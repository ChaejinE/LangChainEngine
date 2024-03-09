from abc import ABCMeta
from typing import Any
from engine_logger.langchain_logger import logger


class BasePrompt(metaclass=ABCMeta):
    def __init__(self, prompt: Any = None) -> None:
        self._prompt = prompt

    @property
    def prompt(self) -> Any:
        return self._prompt

    @prompt.setter
    def prompt(self, prompt: Any):
        self._prompt = prompt
