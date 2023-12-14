import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
from dotenv import load_dotenv
import logging as log
import pandas as pd
import os
import datetime


# Load environment variables
load_dotenv()

# Set logging level
log.basicConfig(level=log.INFO)

# Set your Spotify API credentials
username = os.getenv('SPOTIPY_USERNAME')
client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

redirect_uri = 'http://localhost:8080'  # Replace with your Redirect URI

# Define the scope of access
scope = 'user-library-read'

def get_saved_songs():
    # Fetch the first page of saved tracks
    results = spotify.current_user_saved_tracks(limit=50)

    # Prepare data for CSV
    data = []
    i = 0

    while results:
        for item in results['items']:
            track = item['track']
            data.append((track['name'], track['artists'][0]['name'], track['album']['name'], track['id'], item['added_at']))
        
        # Fetch the next page of results
        if results['next']:
            i += 1
            results = spotify.next(results)
            log.info(f'Fetching page {i} of results...')
            log.info(f'Total results: {50*i}')
        elif i > 400:
            results = None
        else:
            results = None

    # Write data to CSV
    df = pd.DataFrame(data, columns=['Name', 'Artist', 'Album', 'Spotify ID', 'Added On'])
    timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"csv/{username}'s_saved_songs_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename

def get_playlist_songs(playlist_id):
    # Fetch the first page of saved tracks
    results = spotify.playlist_tracks(playlist_id)

    # Prepare data for CSV
    data = []
    i = 0

    while results:
        for item in results['items']:
            track = item['track']
            data.append((track['name'], track['artists'][0]['name'], track['album']['name'], track['id'], item['added_at']))
        
        # Fetch the next page of results
        if results['next']:
            i += 1
            results = spotify.next(results)
            log.info(f'Fetching page {i} of results...')
            log.info(f'Total results: {20*i}')
        else:
            results = None

    # Write data to CSV
    df = pd.DataFrame(data, columns=['Name', 'Artist', 'Album', 'Spotify ID', 'Added On'])
    timestamp = datetime.datetime.now().strftime("%d%m%Y_%H%M%S")
    filename = f"csv/{username}'s_playlist_{playlist_id}_{timestamp}.csv"
    df.to_csv(filename, index=False)
    return filename

def add_song_to_queue(song_id):
    """Adds a song to the queue"""
    spotify.add_to_queue(song_id)

def get_genres():
    """Gets all the genres considered in Spotify's API"""
    genres = spotify.recommendation_genre_seeds()
    log.info(genres)
    return genres

def get_song_features(song_id):
    # Fetch the first page of saved tracks
    results = spotify.audio_features(song_id)
    log.info(results)
    return results[0]

def get_song_analysis(song_id):
    # Fetch the first page of saved tracks
    results = spotify.audio_analysis(song_id)
    log.info(results)
    return results

if __name__ == '__main__':
    get_saved_songs()