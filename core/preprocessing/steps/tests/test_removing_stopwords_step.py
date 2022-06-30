import unittest

from core.models.emotional_text import EmotionalText
from core.models.token import Token
from core.preprocessing.steps.removing_stopwords_step import RemovingStopwordsStep


class TestRemovingStopwordsStep(unittest.TestCase):

    def test_remove_stopwords(self):
        step = RemovingStopwordsStep()
        expected = [Token("Hello")]
        input = [Token("Hello"), Token("a"),Token("I"),Token("the"),]
        self.assertEqual(expected, step.execute(input))

    def test_keep_no_stopwords(self):
        step = RemovingStopwordsStep()
        expected = [Token("Hello"), Token("car"),Token("boy")]
        input = [Token("Hello"), Token("car"),Token("boy")]
        self.assertEqual(expected, step.execute(input))


if __name__ == '__main__':
    unittest.main()
