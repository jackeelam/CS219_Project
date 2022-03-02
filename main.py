import sys
import spotipy
import spotipy.util as util
from pprint import pprint
from spotify_search_play import spotify

CLIENT_ID = "bc5acc7719dd4922bd6b5a92c50c52f6"
CLIENT_SECRET = "c0f0176250cb4906b257c4f416228889"

initialize_tags = False

#MAIN CODE
sp = spotify(username = 'jackeelam', client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
num_tags = len(sp.song_dict)
#while loop that waits for user input
while True:
    song = input("Enter song to play:")
    print("Playing song: ", song)
    #Get the spotify track id for the song
    track_uri = sp.get_track_uri(song)
    #Physically iteratate through the tags to get tag id and compare if spotify track id matches the value in dict
    for i in range(num_tags):
        #TODO: Rotate to position i

        #Read the tag id 
        tag_id = "tag" + str(i) #TODO: change to what is read by arduino and sent via serial monitor
        #If match, just play song
        if (sp.song_dict[tag_id] == track_uri):
            print("Song found in tag")
            sp.play_song(sp.song_dict[tag_id])
            break
        #else if last tag and no match, update song dict and play song
        elif(i == num_tags-1 and sp.song_dict[tag_id] != track_uri):
            print("Overwriting song dictionary")
            sp.song_dict[tag_id] = track_uri
            sp.play_song(sp.song_dict[tag_id])
            print("New song dict", sp.song_dict)
            


    
