from loader.base import BaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from langchain_logger import logger

import sys


class ThesisSummaryLoader(BaseLoader):
    def __init__(self, file_path: str) -> None:
        super().__init__()
        self._loader = PyPDFLoader(file_path=file_path, extract_images=True)
        self._spliter = RecursiveCharacterTextSplitter()

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
