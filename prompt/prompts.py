from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.messages.base import BaseMessage
from prompt.base import BasePrompt
from engine_logger.langchain_logger import logger
from typing import Union, List


class ThesisSummaryPrompt(BasePrompt):
    def __init__(self) -> None:
        self._system_message: Union[SystemMessage, None] = None
        self._human_message: Union[HumanMessage, None] = None

    @property
    def system_message(self) -> Union[SystemMessage, None]:
        return self._system_message

    @system_message.setter
    def system_message(self, msg: SystemMessage):
        logger.debug(f"Success to set system message : {msg}")
        self._system_message = msg

    @property
    def human_message(self) -> Union[HumanMessage, None]:
        return self._human_message

    @human_message.setter
    def human_message(self, msg: HumanMessage):
        logger.debug(f"Success to set human message : {msg}")
        self._human_message = msg

    def generate_template(
        self, system_prompt_template: str = "", human_prompt_template: str = "", **kargs
    ) -> Union[ChatPromptTemplate, List[BaseMessage]]:
        if system_prompt_template:
            self.system_message = SystemMessage(content=system_prompt_template)
            assert (
                self.system_message and self.system_message.content
            ), "Please setup system prompt"
        if human_prompt_template:
            self.human_message = HumanMessage(content=human_prompt_template)
            assert (
                self.human_message and self.human_message.content
            ), "Please setup human prompt"

        try:
            self.prompt_template = ChatPromptTemplate.from_messages(
                [
                    ("system", self.system_message.content),
                    ("human", self.human_message.content),
                ]
            )

            if kargs:
                self.prompt_template = self.prompt_template.format_messages(**kargs)

            logger.debug(
                f"Success to generate prompt template : {self.prompt_template}"
            )

        except Exception as e:
            logger.debug(f"Fail to generate template\n{e}")
            raise e

        return self.prompt_template


class ThesisSummaryMapPrompt(ThesisSummaryPrompt):
    def __init__(self) -> None:
        super().__init__()
        self._map_document_variable: str = ""

    @property
    def map_document_variable(self):
        if not self._map_document_variable:
            raise ValueError(
                f"map document variable is invalid value : {self._map_document_variable}, {type(self._map_document_variable)}"
            )
        return self._map_document_variable

    @map_document_variable.setter
    def map_document_variable(self, val):
        self._map_document_variable = val

    def generate_map_template(self):
        map_system_prompt_template: str = (
            "You are the best AI thesis summary assistant about pages. This is partial of documents. Please summary about this page well."
        )
        map_partial_document_prompt_template: str = (
            "{" + self.map_document_variable + "}"
        )

        map_prompt_template = self.generate_template(
            system_prompt_template=map_system_prompt_template,
            human_prompt_template=map_partial_document_prompt_template,
        )
        logger.info(f"Map prompt template : {map_prompt_template}")

        return map_prompt_template


class ThesisSummaryReducePrompt(ThesisSummaryPrompt):
    def __init__(self) -> None:
        super().__init__()
        self._reduce_document_variable: str = ""

    @property
    def reduce_document_variable(self):
        if not self._reduce_document_variable:
            raise ValueError(
                f"reduce document variable is invalid value : {self._reduce_document_variable}, {type(self._reduce_document_variable)}"
            )
        return self._reduce_document_variable

    @reduce_document_variable.setter
    def reduce_document_variable(self, val):
        self._reduce_document_variable = val

    def generate_reduce_template(self):
        reduce_system_prompt_template: str = "{" + self.reduce_document_variable + "}"
        reduce_partial_document_prompt_template: str = (
            "You are the best AI thesis summary assistant about documents. This is set of thesis summary. Please summary about this set well."
        )

        reduce_prompt_template = self.generate_template(
            system_prompt_template=reduce_system_prompt_template,
            human_prompt_template=reduce_partial_document_prompt_template,
        )
        logger.info(f"Reduce prompt template : {reduce_prompt_template}")

        return reduce_prompt_template
