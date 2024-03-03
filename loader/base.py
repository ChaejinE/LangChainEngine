from abc import ABCMeta, abstractmethod
from typing import Union


class BaseLoader(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def load(self) -> str:
        pass
