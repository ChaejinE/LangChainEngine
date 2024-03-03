from unittest import TestCase
from loader.loaders import ThesisSummaryLoader
from loader.utils import download_file_from_url
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger


class LoadPdfTest(TestCase):
    def setUp(self) -> None:
        url = "https://arxiv.org/pdf/1706.03762.pdf"
        self._pdf_path: str = "./transformer.pdf"
        download_file_from_url(url=url, save_path=self._pdf_path)
        self._loader = ThesisSummaryLoader(file_path=self._pdf_path)
        return super().setUp()

    def tearDown(self) -> None:
        import os

        os.remove(self._pdf_path)
        return super().tearDown()

    def test_load(self):
        content = self._loader.load()
        self.assertIsInstance(content, list)
        if content and len(content) > 0:
            self.assertIsInstance(content[0], Document)
        else:
            logger.info(f"{__file__}\nDocument Length is : {len(content)}")
