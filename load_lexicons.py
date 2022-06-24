from core.emotional_analysis.lexicon_approach.lexicons.nrc_emotions_lexicon import NRCEmotionLexicon
from core.emotional_analysis.lexicon_approach.lexicons.nrc_hashtag_lexicon import NRCHashtagLexicon

print("- LOADING NRC_EMOTION INTO DATABASE...")
nrc_emotion_loaded=NRCEmotionLexicon().load_into_database("files/nrc-emotion.txt")
if nrc_emotion_loaded:
    print("- NRC_EMOTION LOADED TO DATABASE")
else:
    print("- AN ERROR HAS OCCURRED")

print("- LOADING NRC_HASHTAG INTO DATABASE...")
nrc_emotion_loaded=NRCHashtagLexicon().load_into_database("files/nrc-hashtag.txt")
if nrc_emotion_loaded:
    print("- NRC_HASHTAG LOADED TO DATABASE")
else:
    print("- AN ERROR HAS OCCURRED")