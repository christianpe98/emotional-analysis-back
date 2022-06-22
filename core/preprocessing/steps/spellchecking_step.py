from typing import List

from core.models.emotional_text import EmotionalText
from core.preprocessing.steps.preprocessing_step import PreprocessingStep
from core.models.token import Token
import pkg_resources
from symspellpy import SymSpell, Verbosity

class SpellcheckingStep(PreprocessingStep):
    def __init__(self):
        self.sym_spell = SymSpell(max_dictionary_edit_distance=2, prefix_length=7)
        dictionary_path = pkg_resources.resource_filename(
            "symspellpy", "frequency_dictionary_en_82_765.txt"
        )
        # term_index is the column of the term and count_index is the
        # column of the term frequency
        self.sym_spell.load_dictionary(dictionary_path, term_index=0, count_index=1)

    def execute(self, tokens: List[Token]) -> List[Token]:
        corrections=[]
        for token in tokens:
            suggestions = self.sym_spell.lookup(token.text, Verbosity.CLOSEST, max_edit_distance=2, include_unknown=True)
            corrections.append(Token(suggestions[0].term,token.pos_tag))
        return corrections
