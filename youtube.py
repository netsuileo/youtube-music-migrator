from typing import List, Callable
import ytmusicapi
from tqdm import tqdm

from playlist import Playlist, PlaylistItem


def Logger(quiet=False):
    if quiet:
        return lambda: ...
    return print


def ProgressBar(quiet=False):
    if quiet:
        return lambda l: l
    return tqdm


def upload_playlist(playlist: Playlist, auth_headers_file: str, quiet=False):
    ytmusic = ytmusicapi.YTMusic(auth_headers_file)
    logger = Logger(quiet=quiet)
    progress_bar = ProgressBar(quiet=quiet)

    tracklist = progress_bar(playlist["tracks"])

    logger("Searching for tracks")
    ytm_tracks = [find_track(ytmusic, logger, t) for t in tracklist]

    logger("Creating playlist...")
    playlist_id = ytmusic.create_playlist(
        title=playlist["name"], description=playlist["description"]
    )

    video_ids_chunks = progress_bar(chunk_by([t for t in ytm_tracks if t], 10))
    for chunk in video_ids_chunks:
        ytmusic.add_playlist_items(
            playlistId=playlist_id, videoIds=chunk, duplicates=True
        )
    logger("Done!")


def find_track(
    ytmusic: ytmusicapi.YTMusic, logger: Callable, playlist_item: PlaylistItem
) -> str:
    query = f"{playlist_item['artist']} {playlist_item['name']}"
    results = ytmusic.search(query=query, filter="songs")
    if not results:
        logger(f"Track {query} was not found, skipping it.")
        return None
    return results[0]["videoId"]


def chunk_by(source: List, length=int) -> List[List]:
    return [source[i:i+length] for i in range(0, len(source), length)]
