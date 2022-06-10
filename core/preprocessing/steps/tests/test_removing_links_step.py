import unittest

from core.model.emotional_text import EmotionalText
from core.model.token import Token
from core.preprocessing.steps.removing_links_step import RemovingLinksStep


class TestRemovingLinksStep(unittest.TestCase):
    def setUp(self) -> None:
        self.emotional_text = EmotionalText("https://example.com example.com example")
        self.emotional_text.tokens_preprocessed = [Token("https://example.com"), Token("http://example.com"),
                                                   Token("example.com"), Token("example")]

    def test_something(self):
        step = RemovingLinksStep()
        expected = EmotionalText("https://example.com example.com example")
        expected.tokens_preprocessed = [Token("example.com"), Token("example")]
        self.assertEqual(expected, step.execute(self.emotional_text))


if __name__ == '__main__':
    unittest.main()
