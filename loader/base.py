from abc import ABCMeta, abstractmethod


class BaseLoader(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def load(self) -> str:
        pass
