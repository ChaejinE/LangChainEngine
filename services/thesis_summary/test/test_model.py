from unittest import TestCase
from model.llms import ThesisSummaryModel
from engine_logger.langchain_logger import logger


class LoadModelTest(TestCase):
    def setUp(self) -> None:
        self.model_manager = ThesisSummaryModel(model_name="gpt-3.5-turbo-0125")
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_load(self) -> None:
        model = self.model_manager.model
        logger.info(f"Model type : {type(model)}")
