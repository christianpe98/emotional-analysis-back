from core.emotional_analysis.emotional_analysis import EmotionalAnalysis

from core.emotional_analysis.ml_approach.ml_model import MLModel
from core.model.emotional_text import EmotionalText


class EmotionalAnalysisML(EmotionalAnalysis):
    def __init__(self, ml_model: MLModel, vectorizer):
        self.ml_model = ml_model
        self.vectorizer = vectorizer

    def analyze(self, emotional_text: EmotionalText) -> EmotionalText:
        input = self.vectorizer.transform([emotional_text.tokens_preprocessed_string()])
        emotional_text.predominant_emotions = [self.ml_model.predict(input)[0]]
        return emotional_text
