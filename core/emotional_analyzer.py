from core.emotional_analysis.emotional_analysis import EmotionalAnalysis
from core.model.emotional_text import EmotionalText
from core.preprocessing.preprocessor import Preprocessor


class EmotionalAnalyzer:
    def __init__(self,analysis_method:EmotionalAnalysis,preprocessor=Preprocessor()):
        self.preprocessor=preprocessor
        self.analysis_method=analysis_method

    def execute(self,text):
        tokens = self.preprocessor.preprocess(text)
        ed = self.analysis_method.analyze(EmotionalText(text, tokens))
        return ed