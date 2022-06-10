import tweepy
import os
from tweepy import Tweet
from dotenv import load_dotenv

from core.model.tweet import Tweet
from core.model.user_info import UserInfo

load_dotenv()


class TwitterHandler:
    def __init__(self,
                 bearer_token=os.getenv('BEARER_TOKEN'),
                 consumer_key=os.getenv('CONSUMER_KEY'),
                 consumer_secret=os.getenv('CONSUMER_SECRET'),
                 access_token=os.getenv('ACCESS_TOKEN'),
                 access_token_secret=os.getenv('ACCESS_TOKEN_SECRET'),
                 ):
        self.client = tweepy.Client(
            bearer_token, consumer_key, consumer_secret, access_token, access_token_secret,wait_on_rate_limit=True)

    def getUserId(self, username):
        user_id = self.client.get_user(username=username).data.id
        if user_id is None:
            raise ValueError(
                {"message": "Doesn't exist a user with the username: " + self.username, "code": "username-no-exist"})
        return user_id

    def getUserProfileInfo(self, username,user_fields=["created_at", "profile_image_url", "description", "public_metrics"]):
        data = self.client.get_user(username=username, user_fields=user_fields).data
        if data is None:
            return None
        return UserInfo(data)

    def getTweetsFromUsername(self, username, start_time=None,end_time=None):
        user_id = self.getUserId(username)
        tweets=[]
        for tweet in tweepy.Paginator(self.client.get_users_tweets, user_id,start_time=start_time,end_time=end_time, tweet_fields=["created_at"],
                                      exclude=["retweets", "replies"]).flatten():
            tweets.append(Tweet(tweet_id=tweet.id, text=tweet.text, date=tweet.created_at))
        return tweets
