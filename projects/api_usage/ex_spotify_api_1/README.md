## Spotify REST API Metadata Explorer
This is a very simple example to explore Music Metadata from Spotify.

* We use Spotify Web API to retrieve metadata about music artists, albums, 
and tracks, directly from the Spotify Data Catalogue.
  * Web API | Spotify for Developers
  https://developer.spotify.com/documentation/web-api/
  https://developer.spotify.com/documentation/general/guides/authorization/
  https://developer.spotify.com/documentation/general/guides/authorization/app-settings/

* We use Spotipy package for the Spotify Web API:
  * Welcome to Spotipy! — spotipy 2.0 documentation
  https://spotipy.readthedocs.io/

* An API key is needed to request the API
  * Regarding this example you must create the folder spotify_api_keys in the HOME directory
    with a file containing your API public key (spotify_public_key.key)
    and another file containing your API private key spotify_private_key.key
    You can copy this directory structure from the extra folder of this project.
