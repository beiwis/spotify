import os
import spotipy
from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth

load_dotenv()

# Set your Spotify API credentials
username = os.getenv('SPOTIPY_USERNAME')
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

# Define the scope of access
scope = 'user-library-read'

# Create an instance of SpotifyOAuth
auth_manager = SpotifyOAuth(client_id=client_id, client_secret=client_secret, redirect_uri='http://localhost:8080', scope=scope)

# Pass the auth_manager to Spotify
spotify = spotipy.Spotify(auth_manager=auth_manager)

# Now you can access the user's saved tracks
results = spotify.current_user_saved_tracks()