from typing import List

from nltk.tokenize import TweetTokenizer
from core.models.token import Token
from nltk.tokenize.api import TokenizerI
from nltk import pos_tag


class TokenizationStep:

    def __init__(self, tokenizer: TokenizerI = TweetTokenizer(), pos_tagging: bool = True):
        self.tokenizer = tokenizer
        self.pos_tagging = pos_tagging

    def execute(self, text: str) -> List[Token]:
        tokens = self.tokenizer.tokenize(text)
        if self.pos_tagging:
            tuples = pos_tag(tokens)
            return list(map(lambda tuple: Token(tuple[0], tuple[1]), tuples))
        return list(map(lambda text: Token(text), tokens))
