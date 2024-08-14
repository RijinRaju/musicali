from fastapi import FastAPI
from app.api.v1.spotifyApi import music_route
from app.api.v1.emotions import emotion_route
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title='Musicali',
    description="music app based on emotion detection."
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(music_route, )
app.include_router(emotion_route)
