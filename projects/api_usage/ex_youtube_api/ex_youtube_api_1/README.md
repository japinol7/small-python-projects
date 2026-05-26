# Getting YouTube Live Chat messages from REST API
    Example usage of YouTube Data API v3 for reading livestream chat messages.
<br>

	version: 0.1.1
	author: Joan A. Pinol
	author_nickname: japinol
	author_gitHub: japinol7
	author_twitter: @japinol
<br>

	Dependencies:
      * requests
	Python requires: 3.14 or greater.
<br>


## YouTube API Official documentation

Note that you will need to get an API key from Google Cloud to use this integration. <br>
We use this API for this project: YouTube Data API v3.

* https://developers.google.com/youtube/v3
* https://developers.google.com/youtube/v3/live/docs
* https://developers.google.com/youtube/v3/live/docs/liveChatMessages/list
* https://developers.google.com/youtube/v3/docs/videos/list

<br><br>

# Create a YouTube Data API key

Warning: Do not put your Secret keys or passwords in the repo.

Regarding this example, you must create the folder youtube_secrets
in your HOME directory with a file containing your secret key or password.

Recommended tree from your $HOME directory:
* .api_keys
  * youtube_secrets
    * youtube_secrets_api_key.key

<br><br>

**To make the example of usage to work**

	Do this:
	    1. Clone this repository in your local system.
	    2. Go to its folder in your system.
	    3. $ pip install -r requirements.txt
	    4. $ python example_of_usage.py
