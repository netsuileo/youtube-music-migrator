import argparse

import spotify
import youtube


def main():
    arguments = parse_arguments()
    playlist_id = spotify.parse_link_and_get_playlist_id(arguments.source)
    playlist = spotify.get_playlist(
        playlist_id=playlist_id,
        client_id=arguments.spotify_client_id,
        client_secret=arguments.spotify_client_secret,
    )
    youtube.upload_playlist(
        playlist,
        auth_headers_file=arguments.ytm_auth_headers_file,
        quiet=arguments.quiet,
    )


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=str, required=True)
    parser.add_argument("--spotify-client-id", type=str, required=True)
    parser.add_argument("--spotify-client-secret", type=str, required=True)
    parser.add_argument("--ytm-auth-headers-file", type=str, required=True)
    parser.add_argument("--quiet", type=bool, required=False, default=False)
    return parser.parse_args()


if __name__ == "__main__":
    main()
