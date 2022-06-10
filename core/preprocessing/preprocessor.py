from typing import List

from core.preprocessing.steps.filtering_by_pos_tagging_step import FilteringByPosTaggingStep, PosTags
from core.preprocessing.steps.lemmatization_step import WordnetLemmatizerStep
from core.preprocessing.steps.removing_hashtags_step import RemovingHashtagsStep
from core.preprocessing.steps.removing_links_step import RemovingLinksStep
from core.preprocessing.steps.removing_stopwords_step import RemovingStopwordsStep
from core.preprocessing.steps.spellchecking_step import SpellcheckingStep
from core.preprocessing.steps.tokenization_step import TokenizationStep
from core.model.token import Token


class Preprocessor:

    default_steps=[ RemovingLinksStep(),RemovingHashtagsStep(),RemovingStopwordsStep(),WordnetLemmatizerStep(use_pos_tags=True),SpellcheckingStep(),FilteringByPosTaggingStep(
            [PosTags.VERB, PosTags.ADJECTIVES, PosTags.ADVERB, PosTags.NOUN])]

    def __init__(self, steps=default_steps, tokenizer=TokenizationStep()):
        self.steps = steps
        self.tokenizer=tokenizer

    def preprocess(self, text: str) -> List[Token]:
        tokens = self.tokenizer.execute(text)
        for step in self.steps:
            tokens = step.execute(tokens)
        return tokens
