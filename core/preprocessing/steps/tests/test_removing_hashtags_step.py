import unittest

from core.models.token import Token
from core.preprocessing.steps.removing_hashtags_step import RemovingHashtagsStep


class TestRemovingHashtagsStep(unittest.TestCase):
    def test_remove_hashtag(self):
        step = RemovingHashtagsStep()
        expected = [Token("Hello")]
        input = [Token("Hello"), Token("#hello")]
        self.assertEqual(expected, step.execute(input))

    def test_keep_no_hashtag(self):
        step = RemovingHashtagsStep()
        expected = [Token("Hello"), Token("hello")]
        input = [Token("Hello"), Token("hello")]
        self.assertEqual(expected, step.execute(input))


if __name__ == '__main__':
    unittest.main()
