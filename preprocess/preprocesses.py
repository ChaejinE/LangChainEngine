from preprocess.base import BasePreprocess
from preprocess.loader.loaders import ThesisSummaryLoader
from preprocess.prompt.prompts import ThesisSummaryPrompt


class ThesisSummaryPreprocess(BasePreprocess):
    def __init__(self, file_path: str = "", file_uri: str = "") -> None:
        super().__init__()
        self._loader: ThesisSummaryLoader = ThesisSummaryLoader(
            file_path=file_path, file_uri=file_uri
        )
        self._prompt_manager: ThesisSummaryPrompt = ThesisSummaryPrompt()

    @property
    def system_prompt(self):
        return self._prompt_manager.system_message.content

    @system_prompt.setter
    def system_prompt(self, prompt: str):
        self._prompt_manager.system_message = prompt

    @property
    def human_prompt(self):
        return self._prompt_manager.human_message.content

    @human_prompt.setter
    def human_prompt(self, prompt: str):
        self._prompt_manager.human_message = prompt

    def run(self, system_prompt: str, human_prompt: str, inputs: dict[str, str]):
        # load data
        documents = self._loader.load()

        # make prompt
        self.system_prompt = system_prompt
        self.human_prompt = human_prompt
        self._prompt_manager.generate(**inputs)
