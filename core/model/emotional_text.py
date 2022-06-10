from typing import List
from core.model.emotional_token import EmotionalToken
from core.model.token import Token


class EmotionalText:
    def __init__(self, text: str, tokens: List[Token]):
        self._text_original: str = text
        self.tokens_preprocessed: List[Token] = tokens
        self.emotions_in_tokens: List[EmotionalToken] = []
        self._predominant_emotions: List[str] = []

    @property
    def text_original(self):
        return self._text_original

    @property
    def predominant_emotions(self):
        if not self._predominant_emotions:
            return ["none"]
        else:
            return self._predominant_emotions

    @predominant_emotions.setter
    def predominant_emotions(self, value: List[str]):
        self._predominant_emotions = value

    def tokens_preprocessed_string(self):
        return " ".join([token.text for token in self.tokens_preprocessed])

    def as_dict(self):
        tokens_original = list(map(lambda t: t.as_dict(), self.tokens_original))
        tokens_preprocessed = list(map(lambda t: t.as_dict(), self.tokens_preprocessed))
        emotions_in_tokens = list(map(lambda t: t.as_dict(), self.emotions_in_tokens))
        return {
            'text_original': self.text_original,
            'tokens_original': tokens_original,
            'tokens_preprocessed': tokens_preprocessed,
            'emotions_in_tokens': emotions_in_tokens,
            'predominant_emotions': self.predominant_emotions
        }

    def __repr__(self):
        return str(self.as_dict())

    def __str__(self):
        return str(self.as_dict())

    def __eq__(self, other):
        if not isinstance(other, EmotionalText):
            return False
        same_text_original = self.text_original == other.text_original
        same_tokens_original = self.tokens_original == other.tokens_original
        same_tokens_preprocessed = self.tokens_preprocessed == other.tokens_preprocessed
        same_emotions_in_tokens = self.emotions_in_tokens == other.emotions_in_tokens
        same_predominant_emotions = self.predominant_emotions == other.predominant_emotions

        return same_text_original & same_tokens_original & same_tokens_preprocessed \
               & same_emotions_in_tokens & same_predominant_emotions
