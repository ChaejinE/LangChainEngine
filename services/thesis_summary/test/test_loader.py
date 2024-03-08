import os, sys

sys.path.append(
    os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__))))
)

from unittest import TestCase
from loader.loaders import ThesisSummaryLoader
from loader.utils import download_file_from_url
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger


class LoadPdfTest(TestCase):
    def setUp(self) -> None:
        url = "https://arxiv.org/pdf/1706.03762.pdf"
        self._loader = ThesisSummaryLoader(file_uri=url)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_load(self):
        content = self._loader.load()
        self.assertIsInstance(content, list)
        if content and len(content) > 0:
            self.assertIsInstance(content[0], Document)
        else:
            logger.info(f"{__file__}\nDocument Length is : {len(content)}")
