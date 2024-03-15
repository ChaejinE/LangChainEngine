from loader.base import BaseLoader
from loader.utils import download_file_from_url
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger

import sys
import os


class ThesisSummaryLoader(BaseLoader):
    def __init__(self) -> None:
        super().__init__()
        self._file_path: str = ""

    def is_download(self):
        result = os.path.exists(self._file_path)
        logger.info(f"Is Donwloaded ? : {result}")
        return result

    def load(self, input_dict: dict) -> list[Document]:
        try:
            file_uri = input_dict.get("file_uri", "")
            self._file_path = input_dict.get("file_path", "/tmp/tmp.pdf")

            if file_uri:
                logger.info(f"It would be executed from {file_uri}")
                download_file_from_url(url=file_uri, save_path=self._file_path)
            else:
                logger.info(f"It would be executed from {self._file_path}")

            loader = PyPDFLoader(file_path=self._file_path, extract_images=True)
            documents = loader.load_and_split(
                text_splitter=RecursiveCharacterTextSplitter()
            )
            logger.debug(
                f"{__file__}\n \
                    Success Load Content\n \
                    DocumentSize: {len(documents)}\n \
                    ChunkSize: {max(list(map(lambda x: len(x.page_content), documents)))}"
            )
        except Exception as e:
            logger.debug(f"{__file__}\nFail Load Content\n{e}")
            sys.exit(1)

        return documents
