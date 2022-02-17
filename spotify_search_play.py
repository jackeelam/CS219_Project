import sys
import spotipy
import spotipy.util as util
from pprint import pprint

scope = 'user-library-read'

CLIENT_ID = "bc5acc7719dd4922bd6b5a92c50c52f6"
CLIENT_SECRET = "c0f0176250cb4906b257c4f416228889"
token = util.prompt_for_user_token(username='jackeelam', scope=scope, client_id=CLIENT_ID, client_secret=CLIENT_SECRET,redirect_uri="http://google.com/")

if token:
    #Initialize Spotify object so that we can do user related stuff, and call APIs
    sp = spotipy.Spotify(auth=token)

    #Get list of devices and extract device id
    res = sp.devices()
    device_id = res['devices'][0]['id']

    #Search for specific song and get track uri id
    song_to_search = 'war with heaven'#
    search_res = sp.search(q=song_to_search, type='track', limit=1, market='US')
    track_uri = search_res['tracks']['items'][0]['uri']

    #Play track using the track uri
    play = sp.start_playback(device_id = device_id, uris = [track_uri])
else:
    print("Can't get token for", username)