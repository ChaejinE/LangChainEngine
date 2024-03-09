from loader.base import BaseLoader
from loader.utils import download_file_from_url
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger

import sys


class ThesisSummaryLoader(BaseLoader):
    def __init__(self, file_path: str = "", file_uri: str = "") -> None:
        super().__init__()
        self._file_path = file_path
        self._file_uri = file_uri

        if self._file_uri and not self._file_path:
            tmp_file_path = "/tmp/temp.pdf"
            download_file_from_url(url=self._file_uri, save_path=tmp_file_path)
            self._file_path = tmp_file_path

        self._loader = PyPDFLoader(file_path=self._file_path, extract_images=True)
        self._spliter = RecursiveCharacterTextSplitter()

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path

    def load(self) -> list[Document]:
        try:
            documents = self._loader.load_and_split(text_splitter=self._spliter)
            logger.info(
                f"{__file__}\n \
                    Success Load Content\n \
                    DocumentSize: {len(documents)}\n \
                    ChunkSize: {max(list(map(lambda x: len(x.page_content), documents)))}"
            )
        except Exception as e:
            logger.info(f"{__file__}\nFail Load Content\n{e}")
            sys.exit(1)

        return documents
