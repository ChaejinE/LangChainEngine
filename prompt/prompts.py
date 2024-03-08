from langchain.prompts.chat import ChatPromptTemplate
from langchain.prompts import PromptTemplate
from prompt.base import BasePrompt


class ThesisSummaryModel(BasePrompt):
    def __init__(self) -> None:
        self._system_prompt = None
        self._human_prompt = None
        self._prompt = None
        super().__init__(prompt=self._prompt)

    @property
    def system_prompt(self):
        return self._system_prompt

    @system_prompt.setter
    def system_prompt(self, system_prompt: str) -> PromptTemplate:
        self._system_prompt = PromptTemplate(system_prompt)

    @property
    def human_prompt(self):
        return self._human_prompt

    @human_prompt.setter
    def human_prompt(self, human_prompt: str) -> PromptTemplate:
        self._human_prompt = PromptTemplate(human_prompt)

    def generate(self):
        self.system_prompt = "You are a helpful assistant that translates {input_language} to {output_language}."
        self.human_prompt = "{text}"

        self.prompt = ChatPromptTemplate.from_messages(
            [("system", self.system_prompt), ("human", self.human_prompt)]
        )
        print(
            "output : ",
            self.prompt.format_messages(
                input_language="English", output_language="French", text="I love noodle"
            ),
        )
