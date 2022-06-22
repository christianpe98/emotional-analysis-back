from typing import List

from core.models.emotional_text import EmotionalText
from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from enum import Enum

from core.models.token import Token


class PosTags(Enum):
    NOUN = 'NN'
    VERB = 'VB'
    PRONOUN = 'PR'
    ADVERB = 'RB'
    ADJECTIVES = 'JJ'


class FilteringByPosTaggingStep(PreprocessingStep):
    def __init__(self, tags: List[PosTags]):
        self.tags = tags

    def execute(self, tokens:List[Token]) -> List[Token]:
        tokens_result = []
        for token in tokens:
            for tag in self.tags:
                if tag.value in token.pos_tag:
                    tokens_result.append(token)
        return tokens_result