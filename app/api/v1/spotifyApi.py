import pandas as pd
from fastapi import APIRouter
from app.utils.auth import authenticate
from app.api.v1.emotions import identify_emotion
import spotipy
import requests
import os
from dotenv import load_dotenv
from fastapi.responses import RedirectResponse, HTMLResponse

load_dotenv(".env")

music_route = APIRouter()


emotion_mapper = {
    "happy": ["pop", "dance"],
    "sad": ["acoustic", "piano"],
    "angry": ["rock", "metal"],
    "neutral": ["ambient"],
    "surprise": ["electronic"],
    "fear": ["chill"],
    "disgust": ["blues"]
}



@music_route.get('/spotify/get_token', tags=["Spotify"])
async def get_token():
    response = requests.post("https://accounts.spotify.com/api/token",data = {
        "grant_type": "client_credentials",
        "client_id": os.environ.get("CLIENT_ID"),
        "client_secret": os.environ.get("CLIENT_SECRET")
    })
    response_body = response.json()
    access_token = response_body['access_token']
    return access_token



@music_route.post("/spotify/get_song_by_genre", tags=["Spotify"])
async def getSongByGenre(emotion: str):
    genre = emotion_mapper[emotion]
    headers ={
        "Authorization": f"Bearer {await get_token()}"
    }
    params ={
        "seed_artists": "4NHQUGzhtTLFvgF5SZesLK",
        "seed_genres": genre,
        "seed_tracks": "0c6xIDDpzE81m2q797ordA",
    }
    # call the spotify api
    response = requests.get("https://api.spotify.com/v1/recommendations", 
                            headers=headers,params=params)
    return response.json()