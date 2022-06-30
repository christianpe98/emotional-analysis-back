import unittest

from core.models.emotional_text import EmotionalText
from core.models.token import Token
from core.preprocessing.steps.removing_links_step import RemovingLinksStep


class TestRemovingLinksStep(unittest.TestCase):

    def test_remove_link(self):
        step = RemovingLinksStep()
        expected = [Token("Hello")]
        input = [Token("Hello"), Token("https://www.google.com")]
        self.assertEqual(expected, step.execute(input))

    def test_keep_no_link(self):
        step = RemovingLinksStep()
        expected = [Token("Hello"), Token("how")]
        input = [Token("Hello"), Token("how")]
        self.assertEqual(expected, step.execute(input))


if __name__ == '__main__':
    unittest.main()
