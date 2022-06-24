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


class NRCHashtagLexicon(BasicLexicon):
    nrc_all_emotions = [NRCEmotions.JOY, NRCEmotions.FEAR, NRCEmotions.ANGER, NRCEmotions.SADNESS, NRCEmotions.TRUST,
                        NRCEmotions.ANTICIPATION, NRCEmotions.DISGUST, NRCEmotions.SURPRISE]
    nrc_basic_emotions = [NRCEmotions.JOY, NRCEmotions.ANGER, NRCEmotions.FEAR, NRCEmotions.SADNESS]

    def __init__(self, emotions: List[NRCEmotions] = nrc_basic_emotions,
                 database: Database = MongoDB(collection_name="nrc-hashtag-lexicon--4-emotions")):
        super().__init__(emotions, database)

    def load_into_database(self, lexicon_path) -> bool:
        with open(lexicon_path) as f:
            count = 0
            for line in f:
                fields = line.split("\t")
                emotion = NRCEmotions(fields[0])
                keyword = fields[1]
                association = float(fields[2])
                if emotion in self.emotions:  # no almacenamos relaciones con negativos y positivos
                    self.database.create({"keyword": keyword, "emotion": emotion.value, "association": association})
                    count += 1
                    print("count: ", count)
        return True
