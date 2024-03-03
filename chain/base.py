from abc import ABCMeta, abstractmethod


class BaseChain(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def chain(self) -> str:
        pass
