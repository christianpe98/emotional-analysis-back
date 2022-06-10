from re import Pattern
from typing import List

from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from core.model.token import Token


class RemovingByRegexStep(PreprocessingStep):

    def __init__(self, regex: Pattern[str]):
        self.regex = regex

    def execute(self, tokens: List[Token]) -> List[Token]:
        return [token for token in tokens if
                self.regex.match(token.text) is None]
