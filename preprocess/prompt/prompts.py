from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from preprocess.prompt.base import BasePrompt
from typing import Union


class ThesisSummaryPrompt(BasePrompt):
    def __init__(self) -> None:
        self._system_message: Union[SystemMessage, None] = None
        self._human_message: Union[HumanMessage, None] = None

    @property
    def system_message(self) -> Union[SystemMessage, None]:
        return self._system_message

    @system_message.setter
    def system_message(self, prompt: str):
        self._system_message = SystemMessage(content=prompt)

    @property
    def human_message(self) -> Union[HumanMessage, None]:
        return self._human_message

    @human_message.setter
    def human_message(self, prompt: str):
        self._human_message = HumanMessage(content=prompt)

    def generate_template(
        self, system_prompt_template: str = "", human_prompt_template: str = ""
    ) -> ChatPromptTemplate:
        if system_prompt_template:
            self.system_message = system_prompt_template
            assert (
                self.system_message and self.system_message.content
            ), "Please setup system prompt"
        if human_prompt_template:
            self.human_message = human_prompt_template
            assert (
                self.human_message and self.human_message.content
            ), "Please setup human prompt"

        self.prompt_template = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_message.content),
                ("human", self.human_message.content),
            ]
        )
        return self.prompt_template
