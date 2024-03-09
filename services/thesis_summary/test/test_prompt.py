from unittest import TestCase
from preprocess.prompt.prompts import ThesisSummaryPrompt


class PromptTest(TestCase):
    def setUp(self) -> None:
        self.prompt_manager = ThesisSummaryPrompt()
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_generate(self) -> None:
        system_prompt = "You are a helpful assistant that translates {input_language} to {output_language}."
        human_prompt = "{text}"
        kargs = {
            "input_language": "English",
            "output_language": "French",
            "text": "I love noodle",
        }
        ground_truth_sys_propmt = f"You are a helpful assistant that translates {kargs.get('input_language')} to {kargs.get('output_language')}."
        ground_truth_human_prompt = f"{kargs.get('text')}"

        from langchain_core.messages import SystemMessage, HumanMessage

        sys_message, human_message = self.prompt_manager.generate_template(
            system_prompt_template=system_prompt,
            human_prompt_template=human_prompt,
            **kargs,
        )
        # sys_message, human_message = chat_message.format_messages(**kargs)

        self.assertIsInstance(sys_message, SystemMessage)
        self.assertEqual(sys_message.content, ground_truth_sys_propmt)
        self.assertIsInstance(human_message, HumanMessage)
        self.assertEqual(human_message.content, ground_truth_human_prompt)
