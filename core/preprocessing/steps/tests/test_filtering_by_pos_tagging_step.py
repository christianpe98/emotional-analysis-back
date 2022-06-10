import unittest

from core.model.emotional_text import EmotionalText
from core.model.token import Token
from core.preprocessing.steps.filtering_by_pos_tagging_step import FilteringByPosTaggingStep, PosTags


class TestFilteringByPosTaggingStep(unittest.TestCase):
    pos_tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB",
                "RBR", "RBS", "RP", "TO", "UH", "VB", "VBG", "VBD", "VBN", "VBP", "VBZ",
                "WDT", "WP", "WRB"]

    def setUp(self) -> None:
        self.emotional_text = EmotionalText("")
        self.emotional_text.tokens_preprocessed = list(map(lambda tag: Token("", tag), self.pos_tags))

    def test_noun(self):
        step = FilteringByPosTaggingStep([PosTags.NOUN])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "NN"), Token("", "NNS"), Token("", "NNP"), Token("", "NNPS")]
        self.assertEqual(step.execute(self.emotional_text), expected)

    def test_adjectives(self):
        step = FilteringByPosTaggingStep([PosTags.ADJECTIVES])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "JJ"), Token("", "JJR"), Token("", "JJS")]
        self.assertEqual(step.execute(self.emotional_text), expected)

    def test_adverbs(self):
        step = FilteringByPosTaggingStep([PosTags.ADVERB])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "RB"), Token("", "RBR"), Token("", "RBS"), Token("", "WRB")]
        self.assertEqual(step.execute(self.emotional_text), expected)

    def test_verb(self):
        step = FilteringByPosTaggingStep([PosTags.VERB])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "VB"), Token("", "VBG"), Token("", "VBD"), Token("", "VBN"),
                                        Token("", "VBP"), Token("", "VBZ")]
        self.assertEqual(step.execute(self.emotional_text), expected)

    def test_pronoun(self):
        step = FilteringByPosTaggingStep([PosTags.PRONOUN])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "PRP"), Token("", "PRP$")]
        self.assertEqual(step.execute(self.emotional_text), expected)

    def test_pronoun_adj(self):
        step = FilteringByPosTaggingStep([PosTags.PRONOUN, PosTags.ADJECTIVES])
        expected = EmotionalText("")
        expected.tokens_preprocessed = [Token("", "PRP"), Token("", "PRP$"), Token("", "JJ"), Token("", "JJR"),
                                        Token("", "JJS")]
        result = step.execute(self.emotional_text)
        self.assertEqual(len(result.tokens_preprocessed), len(expected.tokens_preprocessed))
        for token in expected.tokens_preprocessed:
            self.assertIn(token, result.tokens_preprocessed)


if __name__ == '__main__':
    unittest.main()
