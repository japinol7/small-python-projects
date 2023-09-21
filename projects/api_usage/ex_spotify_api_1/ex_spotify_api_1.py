import os
from pathlib import Path
from tools.utils import utils
from tools.logger.logger import log

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIFY_API_KEY_FOLDER = os.path.join(str(Path.home()), '.api_keys', 'spotify_api_keys')
SPOTIFY_API_KEY_FILE = os.path.join(SPOTIFY_API_KEY_FOLDER, 'spotify_client_id.key')
SPOTIFY_API_PRIVATE_KEY_FILE = os.path.join(SPOTIFY_API_KEY_FOLDER, 'spotify_client_secret.key')


def main():
    os.environ['SPOTIPY_CLIENT_ID'] = utils.read_file_as_string(SPOTIFY_API_KEY_FILE)
    os.environ['SPOTIPY_CLIENT_SECRET'] = utils.read_file_as_string(SPOTIFY_API_PRIVATE_KEY_FILE)

    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials())

    artist_name = 'Hilary Ha'
    results = spotify.search(q=f'artist:{artist_name}', type='artist')
    items = results['artists']['items']
    if len(items) < 1:
        log.warning(f"Artist not found:{artist_name}")
        return

    if len(items) > 1:
        log.warning(f"Found {len(items)} artists that match the artist name: '{artist_name}'. "
                    f"When searching for albums, we choose the first artist and discard the rest.")

    artist = items[0]
    artist_uri = artist['uri']
    artist_url = artist['external_urls']['spotify']
    followers = artist['followers']['total']
    popularity = artist['popularity']
    log.info(f"Artist: {artist['name']}, followers: {followers} "
             f"popularity: {popularity} uri/url {artist_uri} {artist_url}")

    results = spotify.artist_albums(artist_uri, album_type='album')
    albums = results['items']
    while results['next']:
        results = spotify.next(results)
        albums.extend(results['items'])

    for album in albums:
        log.info(f"Album: {album['name']}")

    log.info(f"{'-' * 15}")
    for artist in items[1:]:
        followers = artist['followers']['total']
        popularity = artist['popularity']
        if followers < 2 and popularity < 1:
            continue
        artist_uri = artist['uri']
        artist_url = artist['external_urls']['spotify']
        log.info(f"--- Another artist: {artist['name']}, followers: {followers} "
                 f"popularity: {popularity} uri/url {artist_uri} {artist_url}")


if __name__ == '__main__':
    main()
