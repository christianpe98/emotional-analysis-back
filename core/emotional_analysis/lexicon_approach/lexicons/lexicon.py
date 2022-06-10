from abc import ABC, abstractmethod
from typing import List
from core.model.emotional_token import EmotionalToken
from core.model.token import Token


class Lexicon(ABC):
    @abstractmethod
    def get_emotion(self, token: Token) -> List[EmotionalToken]:
        pass

    @abstractmethod
    def load_into_database(self, lexicon_path: str) -> bool:
        pass
