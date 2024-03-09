from abc import ABCMeta, abstractmethod
from preprocess.loader.base import BaseLoader
from preprocess.prompt.base import BasePrompt
from typing import Any, Union


class BasePreprocess(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._loader: BaseLoader = None
        self._prompt_manager: BasePrompt = None

    @abstractmethod
    @property
    def system_prompt(self) -> Any:
        pass

    @abstractmethod
    @system_prompt.setter
    def system_prompt(self, prompt: str):
        pass

    @abstractmethod
    @property
    def human_prompt(self) -> Any:
        pass

    @abstractmethod
    @human_prompt.setter
    def human_prompt(self, prompt: str):
        pass

    @abstractmethod
    def run(self, *args, **kargs) -> Any:
        pass
