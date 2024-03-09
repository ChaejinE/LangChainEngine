from chain.base import BaseChain
from langchain.chains import (
    LLMChain,
    StuffDocumentsChain,
    ReduceDocumentsChain,
    MapReduceDocumentsChain,
)
from prompt.prompts import ThesisSummaryPrompt
from model.llms import ThesisSummaryModel
from loader.loaders import ThesisSummaryLoader
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger


class ThesisSummaryChain(BaseChain):
    def __init__(self) -> None:
        super().__init__()
        self._loader = None
        self._map_prompt_template_manager = ThesisSummaryPrompt()
        self._map_llm = ThesisSummaryModel().model
        self._map_chain = None
        self._reduce_prompt_template_manager = ThesisSummaryPrompt()
        self._reduce_llm = ThesisSummaryModel().model
        self._reduce_chain = None

    def invoke(
        self,
        map_document_variable,
        map_system_prompt_template,
        map_user_prompt_template,
        reduce_document_variable,
        reduce_system_prompt_template,
        reduce_user_prompt_template,
        file_path: str = "",
        file_uri: str = "",
        documents: list[Document] = [],
    ) -> str:
        if not documents:
            self._loader = ThesisSummaryLoader(file_path=file_path, file_uri=file_uri)
            documents = self._loader.load()

        map_prompt_template = self._map_prompt_template_manager.generate_template(
            system_prompt_template=map_system_prompt_template,
            human_prompt_template=map_user_prompt_template,
        )
        logger.info(f"Map prompt template : {map_prompt_template}")
        self._map_chain = LLMChain(llm=self._map_llm, prompt=map_prompt_template)
        logger.info("Success to create a map llm chain")

        reduce_prompt_template = self._reduce_prompt_template_manager.generate_template(
            system_prompt_template=reduce_system_prompt_template,
            human_prompt_template=reduce_user_prompt_template,
        )
        logger.info(f"Reduce prompt template : {reduce_prompt_template}")

        reduce_chain = LLMChain(llm=self._reduce_llm, prompt=reduce_prompt_template)
        logger.info("Success to create a reduce llm chain for reduce")
        combined_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain,
            document_variable_name=reduce_document_variable,
        )
        logger.info("Success to create a StuffDocumentsChain for reduce")
        self._reduce_chain = ReduceDocumentsChain(
            combine_documents_chain=combined_documents_chain,
            collapse_documents_chain=combined_documents_chain,
            token_max=4000,
        )
        logger.info("Success to create a ReduceDocumentsChain")

        map_reduce_chain = MapReduceDocumentsChain(
            llm_chain=self._map_chain,
            reduce_documents_chain=self._reduce_chain,
            document_variable_name=map_document_variable,
            return_intermediate_steps=False,
        )
        logger.info("Success to create a MapReduceDocumentsChain")

        if documents or self._loader.is_download():
            result = map_reduce_chain.invoke({"input_documents": documents})
            result = result.get("output_text")
            logger.info(f"Summary : \n{result}")
        else:
            raise RuntimeError("Fail to File Download")

        return result
