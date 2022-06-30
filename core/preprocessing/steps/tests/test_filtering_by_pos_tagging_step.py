import unittest

from core.models.emotional_text import EmotionalText
from core.models.token import Token
from core.preprocessing.steps.filtering_by_pos_tagging_step import FilteringByPosTaggingStep, PosTags


class TestFilteringByPosTaggingStep(unittest.TestCase):
    pos_tags = ["CC", "CD", "DT", "EX", "FW", "IN", "JJ", "JJR", "JJS", "LS",
                "MD", "NN", "NNS", "NNP", "NNPS", "PDT", "POS", "PRP", "PRP$", "RB",
                "RBR", "RBS", "RP", "TO", "UH", "VB", "VBG", "VBD", "VBN", "VBP", "VBZ",
                "WDT", "WP", "WRB"]

    def test_noun(self):
        step = FilteringByPosTaggingStep([PosTags.NOUN])
        expected = [Token("car",pos_tag="NN")]
        input= [Token("car", "NN"), Token("red", "JJ"), Token("there", "RB"), Token("was", "VB")]
        self.assertEqual(expected, step.execute(input))

    def test_adjectives(self):
        step = FilteringByPosTaggingStep([PosTags.ADJECTIVES])
        expected = [Token("red",pos_tag="JJ")]
        input= [Token("car", "NN"), Token("red", "JJ"), Token("there", "RB"), Token("was", "VB")]
        self.assertEqual(expected, step.execute(input))

    def test_adverbs(self):
        step = FilteringByPosTaggingStep([PosTags.ADVERB])
        expected = [Token("there",pos_tag="RB")]
        input= [Token("car", "NN"), Token("red", "JJ"), Token("there", "RB"), Token("was", "VB")]
        self.assertEqual(expected, step.execute(input))

    def test_verb(self):
        step = FilteringByPosTaggingStep([PosTags.VERB])
        expected = [Token("was",pos_tag="VB")]
        input= [Token("car", "NN"), Token("red", "JJ"), Token("there", "RB"), Token("was", "VB")]
        self.assertEqual(expected, step.execute(input))



if __name__ == '__main__':
    unittest.main()
