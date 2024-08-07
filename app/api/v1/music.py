import pandas as pd
from fastapi import APIRouter
from app.utils.auth import authenticate
import spotipy

music_route = APIRouter()

@music_route.get('/get_songs')
async def get_song():
    sp = authenticate()
    artist_name = []
    track_name = []
    popularity = []
    track_id = []
    try:
        for i in range(0,1000,50):
            track_results = sp.search(q='year:2018', type='track', limit=10,offset=i)

            for i, t in enumerate(track_results['tracks']['items']):
                artist_name.append(t['artists'][0]['name'])
                track_name.append(t['name'])
                track_id.append(t['id'])
                popularity.append(t['popularity'])

        track_df = pd.DataFrame({'artist_name' : artist_name,
                                'track_name' : track_name, 
                                'track_id' : track_id, 
                                'popularity' : popularity
                                })
        
        print(track_df.head())
    except spotipy.exceptions.SpotifyException as e:
        print(f"spotify error:{e}")

