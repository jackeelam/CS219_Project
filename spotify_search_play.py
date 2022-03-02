import sys
import spotipy
import spotipy.util as util
from pprint import pprint

class spotify:
    def __init__(self, username, client_id, client_secret):
        self.username = username
        self.client_id = client_id
        self.client_secret = client_secret
        self.scope = ['user-library-read', 'user-read-playback-state', 'user-modify-playback-state']
        self.token = util.prompt_for_user_token(username=self.username, scope=self.scope, client_id= self.client_id, client_secret=self.client_secret,redirect_uri="http://google.com/")
        self.song_dict = self.init_song_dict()
   
    def init_song_dict(self):
        #TODO: REPLACE tag1, tag2, tag3 with the actual tag IDs
        song_dict = {}
        song_dict['tag0'] = "spotify:track:14gmLQPNYokqB8OKxAp69f" #war with heaven
        song_dict['tag1'] = "spotify:track:4ZtFanR9U6ndgddUvNcjcG" #good 4 u
        song_dict['tag2'] = "spotify:track:2dAHKe37uyUrB0v0PJrDDj" #body and mind
        return song_dict
        
    def get_track_uri(self, song):
        if self.token:
            #Initialize Spotify object so that we can do user related stuff, and call APIs
            sp = spotipy.Spotify(auth=self.token)
            #Search for specific song and get track uri id
            song_to_search = song
            search_res = sp.search(q=song_to_search, type='track', limit=1, market='US')
            track_uri = search_res['tracks']['items'][0]['uri']
            print(track_uri)
            return track_uri
        else:
            print("Can't get token for", self.username)

    def play_song(self, track_uri):

        if self.token:
            #Initialize Spotify object so that we can do user related stuff, and call APIs
            sp = spotipy.Spotify(auth=self.token)

            #Get list of devices and extract device id
            res = sp.devices()
            device_id = res['devices'][0]['id']
            play = sp.start_playback(device_id = device_id, uris = [track_uri])
        else:
            print("Can't get token for", self.username)



            


    
