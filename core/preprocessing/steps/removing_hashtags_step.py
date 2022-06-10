import re
from typing import List

from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from core.preprocessing.steps.removing_regex_steps import RemovingByRegexStep
from core.model.token import Token


class RemovingHashtagsStep(PreprocessingStep):

    def __init__(self):
        self.remover = RemovingByRegexStep(re.compile(r'#(\w+)'))

    def execute(self, tokens: List[Token]) -> List[Token]:
        return self.remover.execute(tokens)
