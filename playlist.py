from typing import List, TypedDict


class PlaylistItem(TypedDict):
    artist: str
    song_name: str


class Playlist(TypedDict):
    name: str
    description: str
    tracks: List[PlaylistItem]
