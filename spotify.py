from urllib.parse import urlparse

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

from playlist import Playlist


def parse_link_and_get_playlist_id(spotify_url):
    parsed_url = urlparse(spotify_url)
    return parsed_url.path.split("/")[-1]


def get_playlist(
    client_id: str, client_secret: str, playlist_id: str
) -> Playlist:
    auth_manager = SpotifyClientCredentials(
        client_id=client_id, client_secret=client_secret
    )
    spotify = spotipy.Spotify(auth_manager=auth_manager)
    playlist = spotify.playlist(playlist_id)
    tracks = [
        {
            "artist": track_item["track"]["artists"][0]["name"],
            "name": track_item["track"]["name"],
        }
        for track_item in playlist["tracks"]["items"]
    ]
    return {
        "name": playlist["name"],
        "tracks": tracks,
        "description": f"Imported from Spotify. Playlist id: {playlist_id}",
    }
