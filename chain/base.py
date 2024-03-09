from abc import ABCMeta
from langchain.chains.base import Chain


class BaseChain(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._chain = None

    def create(self, sequence: list):
        for element in sequence:
            if self._chain is None:
                self._chain = element
            else:
                self._chain = self._chain | element

    @property
    def chain(self) -> Chain:
        return self._chain
