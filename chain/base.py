from abc import ABCMeta
from typing import Any
from engine_logger.langchain_logger import logger


class BaseChain(metaclass=ABCMeta):
    def __init__(self) -> None:
        self._chain = None

    @property
    def chain(self) -> Any:
        return self._chain

    @chain.setter
    def chain(self, chain: Any):
        self._chain = chain
        logger.info(f"Success to set chain : {type(self._chain)}")
