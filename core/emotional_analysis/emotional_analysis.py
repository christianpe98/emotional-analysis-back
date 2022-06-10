from abc import ABC, abstractmethod
from core.model.emotional_text import EmotionalText


class EmotionalAnalysis(ABC):
    @abstractmethod
    def analyze(self, emotional_text: EmotionalText) -> EmotionalText:
        pass
