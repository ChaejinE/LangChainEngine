from model.base import BaseLLM
from langchain_openai import ChatOpenAI


class ThesisSummaryModel(BaseLLM):
    def __init__(self, model_name: str = "gpt-3.5-turbo-0125") -> None:
        super().__init__()
        self._model_name: str = model_name
        self.model: ChatOpenAI = ChatOpenAI(temperature=0, name=model_name)

    @property
    def model_name(self) -> str:
        return self._model_name

    @model_name.setter
    def model_name(self, model_name) -> None:
        self.__init__(model_name=model_name)

    def change_model(self, model_name) -> None:
        self.model_name = model_name
