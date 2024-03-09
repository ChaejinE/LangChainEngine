from loader.base import BaseLoader
from loader.utils import download_file_from_url
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.documents.base import Document
from engine_logger.langchain_logger import logger
from threading import Thread, Event

import sys
import os


class ThesisSummaryLoader(BaseLoader):
    def __init__(self, file_path: str = "", file_uri: str = "") -> None:
        super().__init__()
        self._file_path = file_path if file_path else "/tmp/temp.pdf"
        self._file_uri = file_uri
        self._loader = None
        self._spliter = RecursiveCharacterTextSplitter()
        self._thread_event = Event()

    @property
    def file_path(self):
        return self._file_path

    @file_path.setter
    def file_path(self, path):
        self._file_path = path

    def download_file(self, url, save_path):
        logger.info(f"Start to download file from {url}")
        Thread(
            target=download_file_from_url,
            kwargs={"url": url, "save_path": save_path},
        ).start()
        self._thread_event.set()

    def is_download(self):
        self._thread_event.wait(timeout=120)
        result = os.path.exists(self._file_path)
        logger.info(f"Is Donwloaded ? : {result}")
        return result

    def load(self) -> list[Document]:
        try:
            if self._file_uri:
                logger.info(f"It would be executed from {self._file_uri}")
                self.download_file(url=self._file_uri, save_path=self._file_path)
            else:
                logger.info(f"It would be executed from {self._file_path}")
                self._thread_event.set()

            self._loader = PyPDFLoader(file_path=self._file_path, extract_images=True)
            documents = self._loader.load_and_split(text_splitter=self._spliter)
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
