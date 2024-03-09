from chain.base import BaseChain
from prompt.prompts import ThesisSummaryPrompt
from model.llms import ThesisSummaryModel
from engine_logger.langchain_logger import logger


class ThesisSummaryChain(BaseChain):
    def __init__(self) -> None:
        super().__init__()
        self._map_prompt_template_manager = ThesisSummaryPrompt()
        self._map_llm = ThesisSummaryModel().model
        self._reduce_prompt_template_manager = ThesisSummaryPrompt()
        self._reduce_llm = ThesisSummaryModel().model

    def invoke(
        self,
        map_system_prompt_template,
        map_user_prompt_template,
        reduce_system_prompt_template,
        reduce_user_prompt_template,
        request: dict = dict(),
    ) -> None:
        map_prompt_template = self._map_prompt_template_manager.generate_template(
            system_prompt_template=map_system_prompt_template,
            human_prompt_template=map_user_prompt_template,
        )
        logger.info(f"Map prompt template : {map_prompt_template}")

        reduce_prompt_template = self._reduce_prompt_template_manager.generate_template(
            system_prompt_template=reduce_system_prompt_template,
            human_prompt_template=reduce_user_prompt_template,
        )
        logger.info(f"Reduce prompt template : {reduce_prompt_template}")

        sequence = []

        # self.create(sequence=sequence)
        # result = self.chain.invoke(request)
        # logger.info(f"Result : {result}")
