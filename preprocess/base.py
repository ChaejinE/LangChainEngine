from abc import ABCMeta, abstractmethod
from preprocess.loader.base import BaseLoader
from preprocess.prompt.base import BasePrompt
from typing import Any


class BasePreprocess(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._loader: BaseLoader = None
        self._prompt_manager: BasePrompt = None

    @abstractmethod
    def run(self, *args, **kargs) -> Any:
        pass
