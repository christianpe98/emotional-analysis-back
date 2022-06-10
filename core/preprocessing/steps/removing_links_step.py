import re
from typing import List

from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from core.preprocessing.steps.removing_regex_steps import RemovingByRegexStep
from core.model.token import Token


class RemovingLinksStep(PreprocessingStep):

    def __init__(self):
        link_regex = re.compile(
            r'^(?:http|ftp)s?://'  # http:// or https://
            r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # domain...
            r'localhost|'  # localhost...
            r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'  # ...or ip
            r'(?::\d+)?'  # optional port
            r'(?:/?|[/?]\S+)$', re.IGNORECASE)
        self.remover = RemovingByRegexStep(link_regex)

    def execute(self, tokens: List[Token]) -> List[Token]:
        return self.remover.execute(tokens)
