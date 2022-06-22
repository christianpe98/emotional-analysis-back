import unittest

from core.models.emotional_text import EmotionalText
from core.models.token import Token
from core.preprocessing.steps.removing_hashtags_step import RemovingHashtagsStep


class TestRemovingHashtagsStep(unittest.TestCase):
    def setUp(self) -> None:
        self.emotional_text = EmotionalText("#hello #hello hello# hello#hello # hello")
        self.emotional_text.tokens_preprocessed = [Token("#hello"), Token("hello#"), Token("hello#hello"), Token("#"),
                                                   Token("hello")]

    def test_something(self):
        step = RemovingHashtagsStep()
        expected = EmotionalText("#hello #hello hello# hello#hello # hello")
        expected.tokens_preprocessed = [Token("hello#"), Token("hello#hello"), Token("#"), Token("hello")]
        self.assertEqual(expected, step.execute(self.emotional_text))


if __name__ == '__main__':
    unittest.main()
