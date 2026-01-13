from abc import ABC, abstractmethod


class Media(ABC):
    def __init__(self, title, duration, description):
        self.title = title
        self.duration = duration
        self._description = description

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def genre(self):
        pass

    def info(self):
        print(
            f"Title: {self.title}, Duration: {self.duration}, Description: {self._description}"
        )
