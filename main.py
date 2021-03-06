import sys
import spotipy
import spotipy.util as util
from pprint import pprint
from spotify_search_play import spotify
sys.path.append(".")
import RPi.GPIO as GPIO
import time
import os
from servoFunction import servoFunction
from Read import rfid_reader

rd = rfid_reader()

servoClass = servoFunction()
#https://www.google.com/?code=AQCL7lmEQXDqIMvg_tWPsdYWbkXnB4Yj6PWbuEgSSG3i0ZpPAJm5cxwgxbthiY5zCm5CQGGeKzPyFDvEk-1VtrlvMNyA2bKY0bmaoH2HkLnynl9NqREZQ3d2KEuQ8x7MhL2yBS7xd2V5wcvckj9fFIEQxPeVe5HgAskvdXiLRxGf71gxtZFSyNYCr_n87_3pU55K1yli-MA2N0hXfI2cOHccOwdf5xqYKTJepVUhoh9e2aqpSHy5086uHzhpDPM
CLIENT_ID = "bc5acc7719dd4922bd6b5a92c50c52f6"
CLIENT_SECRET = "c0f0176250cb4906b257c4f416228889"

initialize_tags = False

#MAIN CODE
sp = spotify(username = 'jackeelam', client_id = CLIENT_ID, client_secret = CLIENT_SECRET)
num_tags = len(sp.song_dict)
#while loop that waits for user input
while True:
    song = input("Enter song to play:")

    #Get the spotify track id for the song
    track_uri = sp.get_track_uri(song)
    #Physically iteratate through the tags to get tag id and compare if spotify track id matches the value in dict
    for i in range(num_tags):
        #Read the tag id
        tag_id_arr =  rd.read_tag_id() #array of 4 elements of uid
        tag_id = str(tag_id_arr[0]) + str(tag_id_arr[1]) + str(tag_id_arr[2]) + str(tag_id_arr[3])

	#tag_id = "tag" + str(i) #TODO: change to what is read by arduino and sent via serial monitor
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

        elif(i < num_tags-1):
            #TODO: Rotate to position i
            servoClass.rotateMotor(1)

        time.sleep(1)
    time.sleep(2)
    servoClass.reset()
