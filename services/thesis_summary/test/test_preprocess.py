from unittest import TestCase
from preprocess.preprocesses import ThesisSummaryPreprocess

import logging

logging.basicConfig(level=logging.INFO)


class PreprocessTest(TestCase):
    def setUp(self) -> None:
        url = "https://arxiv.org/pdf/1706.03762.pdf"
        self.preprocess = ThesisSummaryPreprocess(file_uri=url)
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_run(self) -> None:
        inputs = {"subject": "thesis"}
        system_prompt = """
            You are the best summary assistant about {subject}
            Please summary on based this contents
            answer :
        """
        user_prompt = "some content"
        prompt_template = self.preprocess.run(
            system_prompt=system_prompt, human_prompt=user_prompt, inputs=inputs
        )
