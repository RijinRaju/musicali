from fastapi import APIRouter
from services.detect_emotion import detect_emotion
from collections import Counter


emotion_route = APIRouter()


@emotion_route.get('/emotion/identify_emotion',tags=["Models"])
async def identify_emotion():

    """
     recognize the face emotion

     Returns:
        facial emotion

    """
    emotion_list = detect_emotion()
    emotion_list = Counter(emotion_list)
    return emotion_list.most_common(1)[0][0]


 