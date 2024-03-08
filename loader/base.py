from abc import ABCMeta, abstractmethod
from typing import Any


class BaseLoader(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def load(self) -> Any:
        pass
