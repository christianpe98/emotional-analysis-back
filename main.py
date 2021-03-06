import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from datetime import datetime
# uvicorn main:app --reload
from core.emotional_analyzer_builder import EmotionalAnalyzerBuilder
from core.twitter.twitter_handler import TwitterHandler

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/api/")
async def running():
    return {"status": "RUNNING"}


@app.get("/api/emotional/approaches")
async def get_emotional_approaches():
    return {"approaches_codes": list(map(lambda option: {"label": option["label"], "code": option["code"]},
                                         EmotionalAnalyzerBuilder.analysis_approaches_options))}


@app.get("/api/emotional")
async def get_emotional_analysis(username: str, start_date: str, end_date: str, analysis_code: str):
    try:
        start_time = datetime.strptime(
            start_date, '%Y-%m-%d').isoformat() + "Z"
        end_time = datetime.strptime(end_date, '%Y-%m-%d')
        end_time = end_time.replace(
            hour=23, minute=59, second=59).isoformat() + "Z"
        tweets = TwitterHandler().get_tweets_from_username(username, start_time, end_time)
        analyzer = EmotionalAnalyzerBuilder.build_emotional_analyzer(
            analysis_code)
        result = []
        for tweet in tweets:
            ed = analyzer.execute(tweet.text)
            result.append({"text": ed.text_original, "emotions": ed.predominant_emotions, "tweet_id": tweet.tweet_id,
                           "date": tweet.date})
        return {"result": result}
    except ValueError as ve:
        print(ve.args[0])
        return {"error": {"message": ve.args[0]["message"], "code": ve.args[0]["code"]}}


@app.get("/api/userinfo")
async def get_user_info(username):
    user_info = TwitterHandler().get_user_profile_info(username)
    return user_info
