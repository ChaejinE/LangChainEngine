from abc import ABCMeta, abstractmethod


class BaseModel(metaclass=ABCMeta):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def get_model(self):
        pass
