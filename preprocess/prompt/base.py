from abc import ABCMeta
from typing import Any
from engine_logger.langchain_logger import logger


class BasePrompt(metaclass=ABCMeta):
    def __init__(self, prompt_template: Any = None) -> None:
        self._prompt_template = prompt_template

    @property
    def prompt_template(self) -> Any:
        return self._prompt_template

    @prompt_template.setter
    def prompt_template(self, prompt_template: Any):
        self._prompt_template = prompt_template
