from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name):
        self._name = name

    @abstractmethod
    def play_media(self, library):
        pass
