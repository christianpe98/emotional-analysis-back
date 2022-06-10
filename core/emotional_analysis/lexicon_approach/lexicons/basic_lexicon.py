from abc import abstractmethod
from typing import List
from core.databases.database import Database
from core.emotional_analysis.lexicon_approach.lexicons.lexicon import Lexicon
from core.model.emotional_token import EmotionalToken
from core.model.token import Token


class BasicLexicon(Lexicon):
    def __init__(self, emotions_recognised: List[str], database: Database):
        self.emotions = emotions_recognised
        self.database = database

    def get_emotion(self, token: Token) -> EmotionalToken:
        return self.database.read(token.text)

    @abstractmethod
    def load_into_database(self, lexicon_path: str) -> bool:
        pass
