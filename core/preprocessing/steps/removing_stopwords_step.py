from typing import List

from core.model.emotional_text import EmotionalText
from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from nltk.corpus import stopwords as storwords_list

from core.model.token import Token


class RemovingStopwordsStep(PreprocessingStep):
    def __init__(self, stopwords: set[str] = set(storwords_list.words('english'))):
        self.stopwords = stopwords

    def execute(self, tokens: List[Token]) -> List[Token]:
        return [token for token in tokens if
                not token.text.lower() in self.stopwords]  # stopwords removed
