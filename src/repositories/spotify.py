import spotipy
from spotipy.oauth2 import SpotifyClientCredentials


def get_song_name_and_artist(spotify_link):
    # Initialize Spotipy client
    client_credentials_manager = SpotifyClientCredentials()
    sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
    track_info = sp.track(spotify_link)
    song_name = track_info['name']
    song_artist = track_info['artists'][0]['name']
    return song_name, song_artist
