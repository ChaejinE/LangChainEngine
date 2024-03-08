from unittest import TestCase
from loader.loaders import ThesisSummaryLoader
from langchain_core.documents.base import Document


class LoadPdfTest(TestCase):
    def setUp(self) -> None:
        url = "https://arxiv.org/pdf/1706.03762.pdf"
        self._loader = ThesisSummaryLoader(file_uri=url)
        return super().setUp()

    def tearDown(self) -> None:
        removed_path = []
        removed_path.append(self._loader.file_path)

        import os

        try:
            for path in removed_path:
                os.remove(path)
        except:
            for path in removed_path:
                os.removedirs(path)

        return super().tearDown()

    def test_load(self):
        content = self._loader.load()
        self.assertIsInstance(content, list)
        self.assertIsInstance(content[0], Document)
