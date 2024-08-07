import spotipy
import os
from spotipy.oauth2 import SpotifyClientCredentials 
from dotenv import load_dotenv


CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')



def authenticate():
    """
    pass the app credentials and get the access and refresh tokens.
    Returns:
        spotipy object
    """
    client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    return sp