from typing import List
from core.databases.mongodb import MongoDB
from core.databases.database import Database
from core.emotional_analysis.lexicon_approach.lexicons.basic_lexicon import BasicLexicon
from enum import Enum


class NRCEmotions(Enum):
    JOY = 'joy'
    ANGER = 'anger'
    SADNESS = 'sadness'
    FEAR = 'fear'
    TRUST = 'trust'
    SURPRISE = 'surprise'
    DISGUST = 'disgust'
    ANTICIPATION = 'anticipation'
    NEGATIVE = 'negative'
    POSITIVE = 'positive'


class NRCEmotionLexicon(BasicLexicon):
    nrc_all_emotions = [NRCEmotions.JOY, NRCEmotions.FEAR, NRCEmotions.ANGER, NRCEmotions.SADNESS, NRCEmotions.TRUST,
                        NRCEmotions.ANTICIPATION, NRCEmotions.DISGUST, NRCEmotions.SURPRISE]
    nrc_basic_emotions = [NRCEmotions.JOY, NRCEmotions.ANGER, NRCEmotions.FEAR, NRCEmotions.SADNESS]

    def __init__(self, emotions: List[NRCEmotions] = nrc_basic_emotions,
                 database: Database = MongoDB(collection_name="nrc-emotion-lexicon--wordlevel_4-emotions")):
        super().__init__(emotions, database)

    def load_into_database(self, lexicon_path) -> bool:
        with open(lexicon_path) as f:
            count = 0
            for line in f:
                fields = line.split("\t")
                keyword = fields[0]
                emotion = NRCEmotions(fields[1])
                association = bool(int(fields[2]))
                if association:  # Solo las keywords que tiene asociación emocional
                    if emotion in self.emotions:  # no almacenamos relaciones con negativos y positivos
                        self.database.create({"keyword": keyword, "emotion": emotion.value})
                        count += 1
                print("count: ", count)
        return True
