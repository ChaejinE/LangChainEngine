from unittest import TestCase, skip
from chain.chains import ThesisSummaryChain

import logging

logging.basicConfig(level=logging.WARNING)


class ChainTest(TestCase):
    def setUp(self) -> None:
        self.url = "https://arxiv.org/pdf/1706.03762.pdf"
        self.chain_manager = ThesisSummaryChain()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    # @skip(reason="Test need the money")
    def test_invoke(self) -> None:
        chain = self.chain_manager.make_chain()
        input = {"file_uri": self.url}
        chain.invoke(input=input)
