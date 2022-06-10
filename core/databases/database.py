from abc import ABC, abstractmethod
from typing import List
from core.model.emotional_token import EmotionalToken


class Database(ABC):
    @abstractmethod
    def create(self, emotional_token: EmotionalToken) -> bool:
        pass

    @abstractmethod
    def read(self, key: str) -> List[EmotionalToken]:
        pass
