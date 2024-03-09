from langchain.prompts.chat import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_core.messages.base import BaseMessage
from prompt.base import BasePrompt
from typing import List


class ThesisSummaryPrompt(BasePrompt):
    def __init__(self) -> None:
        self._system_message: str = ""
        self._human_message: str = ""
        self._prompt: str = ""
        super().__init__(prompt=self._prompt)

    @property
    def system_message(self) -> SystemMessage:
        return self._system_message

    @system_message.setter
    def system_message(self, prompt: str) -> SystemMessage:
        self._system_message = SystemMessage(content=prompt)

    @property
    def human_message(self) -> HumanMessage:
        return self._human_message

    @human_message.setter
    def human_message(self, prompt: str) -> HumanMessage:
        self._human_message = HumanMessage(content=prompt)

    def generate(
        self, system_prompt: str = "", human_prompt: str = "", **kargs
    ) -> List[BaseMessage]:
        self.system_message = system_prompt
        self.human_message = human_prompt

        assert self.system_message.content, "Please setup system prompt"
        assert self.human_message.content, "Please setup human prompt"

        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", self.system_message.content),
                ("human", self.human_message.content),
            ]
        )
        prompt = self.prompt.format_messages(**kargs)
        return prompt
