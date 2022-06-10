from typing import List

from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from core.model.token import Token
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet


class WordnetLemmatizerStep(PreprocessingStep):
    def __init__(self, use_pos_tags: bool):
        self.lemma = WordNetLemmatizer()
        self.use_pos_tags = use_pos_tags

    def execute(self, tokens: List[Token]) -> List[Token]:
        if self.use_pos_tags:
            return [
                Token(self.lemma.lemmatize(token.text, self.getPostag(token.pos_tag)), token.pos_tag) for token in
                tokens]
        return [Token(self.lemma.lemmatize(token.text), token.pos_tag) for token in
                tokens]

    def getPostag(self, pos_tag: str):
        if 'VB' in pos_tag:
            return wordnet.VERB
        if 'RB' in pos_tag:
            return wordnet.ADV
        if 'JJ' in pos_tag:
            return wordnet.ADJ
        else:
            return wordnet.NOUN
