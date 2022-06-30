import unittest

from core.models.token import Token
from core.preprocessing.steps.tokenization_step import TokenizationStep


class TestTokenizationStep(unittest.TestCase):

    def test_tokenization(self):
        step = TokenizationStep(pos_tagging=False)
        expected=[Token("Hello"),Token("how"),Token("are"),Token("you"),Token("?")]
        actual=step.execute("Hello how are you?")
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
