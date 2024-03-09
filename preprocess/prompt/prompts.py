from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.messages.base import BaseMessage
from preprocess.prompt.base import BasePrompt
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
        logger.info(f"Success to set system message : {msg}")
        self._system_message = msg

    @property
    def human_message(self) -> Union[HumanMessage, None]:
        return self._human_message

    @human_message.setter
    def human_message(self, msg: HumanMessage):
        logger.info(f"Success to set human message : {msg}")
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

            logger.info(f"Success to generate prompt template : {self.prompt_template}")

        except Exception as e:
            logger.info(f"Fail to generate template\n{e}")
            raise e

        return self.prompt_template
