from chain.base import BaseChain
from engine_logger.langchain_logger import logger


class ThesisSummaryChain(BaseChain):
    def __init__(self) -> None:
        super().__init__()
        from loader.loaders import ThesisSummaryLoader
        from model.llms import ThesisSummaryModel

        self._loader = ThesisSummaryLoader()
        self._llm = ThesisSummaryModel()

    def invoke(self, request: dict = dict()) -> None:
        sequence = []
        sequence.append(self._loader)
        sequence.append(self._llm)

        self.create(sequence=sequence)
        result = self.chain.invoke(request)
        logger.info(f"Result : {result}")
