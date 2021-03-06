from dotenv import load_dotenv

from core.databases.database import Database
from pymongo import MongoClient
from typing import List
from core.models.emotional_token import EmotionalToken
from core.models.token import Token
import os
load_dotenv()

class MongoDB(Database):

    def __init__(self, collection_name: str, url=os.getenv('MONGO_URL')):
        self.client = MongoClient(url)
        self.database = self.client["lexicons"]
        self.collection_name = collection_name

    def create(self, emotional_token: EmotionalToken) -> bool:
        collection = self.database[self.collection_name]
        collection.insert_one(emotional_token)
        return True

    def read(self, key: str) -> List[EmotionalToken]:
        collection = self.database[self.collection_name]
        mongo_results = list(collection.find({"keyword": key}))
        emotional_tokens = []
        for doc in mongo_results:
            token = Token(doc["keyword"])
            emotion = doc["emotion"]
            if "association" in doc:
                emotional_tokens.append(EmotionalToken(token, emotion, doc["association"]))
            else:
                emotional_tokens.append(EmotionalToken(token, emotion))

        return emotional_tokens
