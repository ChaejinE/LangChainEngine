from chain.base import BaseChain
from engine_logger.langchain_logger import logger


class ThesisSummaryChain(BaseChain):
    def __init__(self) -> None:
        super().__init__()

    def invoke(self, request: dict = dict()) -> None:
        sequence = []

        self.create(sequence=sequence)
        result = self.chain.invoke(request)
        logger.info(f"Result : {result}")
