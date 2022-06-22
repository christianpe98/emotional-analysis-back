from core.emotional_analysis.emotional_analysis import EmotionalAnalysis
from core.models.emotional_text import EmotionalText
from core.emotional_analysis.lexicon_approach.lexicons.lexicon import Lexicon
from typing import List


class EmotionalAnalysisLexicon(EmotionalAnalysis):

    def __init__(self, lexicon: Lexicon):
        self.lexicon = lexicon

    def analyze(self, emotional_text: EmotionalText) -> EmotionalText:
        for token in emotional_text.tokens_preprocessed:
            emotions_obtained=self.lexicon.get_emotion(token)
            emotional_text.emotions_in_tokens.extend(emotions_obtained)
            emotional_text.predominant_emotions=self.get_predominant_emotions(emotional_text)
        return emotional_text

    def get_predominant_emotions(self, emotional_text: EmotionalText) -> List[str]:
        emotions_ranking: dict[str:float] = {}
        for emotion_token in emotional_text.emotions_in_tokens:
            if emotion_token.emotion in emotions_ranking:
                emotions_ranking[emotion_token.emotion] += emotion_token.association
            else:
                emotions_ranking[emotion_token.emotion] = emotion_token.association
        final_emotions=[]
        if emotions_ranking:
            max_value = max(emotions_ranking.values())
            final_emotions =[k for k,v in emotions_ranking.items() if v == max_value]
        return final_emotions
