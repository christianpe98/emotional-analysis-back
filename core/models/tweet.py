from datetime import datetime


class Tweet:
    def __init__(self, tweet_id: str, text: str, date: datetime):
        self.date = date
        self.text = text
        self.tweet_id = tweet_id