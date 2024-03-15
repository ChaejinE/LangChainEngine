from langchain.chains import (
    LLMChain,
    StuffDocumentsChain,
    ReduceDocumentsChain,
    MapReduceDocumentsChain,
)
from prompt.prompts import ThesisSummaryMapPrompt, ThesisSummaryReducePrompt
from model.llms import ThesisSummaryModel
from loader.loaders import ThesisSummaryLoader
from engine_logger.langchain_logger import logger


class ThesisSummaryChain:
    def __init__(self) -> None:
        super().__init__()
        self._loader = ThesisSummaryLoader()
        self._map_prompt_template_manager = ThesisSummaryMapPrompt()
        self._map_llm = ThesisSummaryModel().model
        self._map_chain = None
        self._reduce_prompt_template_manager = ThesisSummaryReducePrompt()
        self._reduce_llm = ThesisSummaryModel().model
        self._reduce_chain = None
        self._chain = None

    @property
    def chain(self):
        return self._chain

    def make_loader_for_chain(self):
        from langchain.schema.runnable import RunnableLambda

        return RunnableLambda(self._loader.load)

    def make_prompt_for_chain(self) -> tuple:
        self._map_prompt_template_manager.map_document_variable = "pages"
        map_prompt_template = self._map_prompt_template_manager.generate_map_template()

        self._reduce_prompt_template_manager.reduce_document_variable = "doc_summaries"
        reduce_prompt_template = (
            self._reduce_prompt_template_manager.generate_reduce_template()
        )

        return (map_prompt_template, reduce_prompt_template)

    def make_chain(self):
        # loader
        loader = self.make_loader_for_chain()

        # prompt
        map_prompt_template, reduce_prompt_template = self.make_prompt_for_chain()

        # basic chain
        self._map_chain = LLMChain(llm=self._map_llm, prompt=map_prompt_template)
        logger.info("Success to create a map llm chain")

        reduce_chain = LLMChain(llm=self._reduce_llm, prompt=reduce_prompt_template)
        logger.info("Success to create a reduce llm chain for reduce")

        combined_documents_chain = StuffDocumentsChain(
            llm_chain=reduce_chain,
            document_variable_name=self._reduce_prompt_template_manager.reduce_document_variable,
        )
        logger.info("Success to create a StuffDocumentsChain for reduce")

        self._reduce_chain = ReduceDocumentsChain(
            combine_documents_chain=combined_documents_chain,
            collapse_documents_chain=combined_documents_chain,
            token_max=4000,
        )
        logger.info("Success to create a ReduceDocumentsChain")

        chain = MapReduceDocumentsChain(
            llm_chain=self._map_chain,
            reduce_documents_chain=self._reduce_chain,
            document_variable_name=self._map_prompt_template_manager.map_document_variable,
            return_intermediate_steps=False,
        )
        logger.info("Success to create a MapReduceDocumentsChain")

        # result chain
        chain = loader | chain
        return chain
