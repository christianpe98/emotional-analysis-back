from abc import ABC, abstractmethod
from typing import List

from core.models.token import Token

class PreprocessingStep(ABC):

    @abstractmethod
    def execute(self, tokens:List[Token]) -> List[Token]:
        pass

