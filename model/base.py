from abc import ABCMeta
from typing import Any
from engine_logger.langchain_logger import logger


class BaseLLM(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._model = None

    @property
    def model(self):
        logger.debug(f"Model type : {type(self._model)}")
        return self._model

    @model.setter
    def model(self, model: Any):
        self._model = model
