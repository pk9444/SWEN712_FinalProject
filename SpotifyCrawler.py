from spotipy.oauth2 import SpotifyClientCredentials #spotify library to process spotify playlists
import spotipy
from pprint import pprint #pretty_print interface to print output in such a way that it can be used as input


class Test():
    '''
    Override Function on_data() to print a data stream
    '''
    def on_data(self, data):
        print(data)
        return True

    '''
    Override Function on_error() to return error in reading a stream if any
    '''
    def on_error(self, status):
        print(status)


'''
    Driver Function
    '''
def main():

    #spotify developer client ID and secret key to enable the API
    cid = 'b2607533769648d8a8da94ec98db6777'
    secret = 'b187275783aa4c76b7be200631f7b5e6'

    '''
          try-except block to handle the authentication provided by the SpotifyClientCredentials interface of spotipy
          @:exception - Checked Exception for failed Authentication 
          '''
    try:
        client_credentials_manager = SpotifyClientCredentials(client_id=cid, client_secret=secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

    except:
        print("Authentication Failed...")

    #take user input for playlist ID from spotify page and store it in variable pl_id
    user_input = input("Enter a playlist ID: ")
    pl_id = 'spotify:playlist:' + user_input
    offset = 1 # offset of 1 indicates output stream at each iteration

    while True:
        #store the mined spotify playlist information in the variable output
        #mine the artist_name as the primary field attribute
        output = sp.playlist_tracks(pl_id, offset=offset, fields='items.track.artists.name,total')
        pprint(output['items']) #print all the items as pretty_print so that it can be used as input
        offset = offset + len(output['items'])
        print(offset, "/", "\t", output['total'])

        #if there are no items in the list, then break from the while true loop and end process
        if len(output['items']) == 0:
            break

# Calling main function
if __name__ == "__main__":
     while(True):
      main()

#--------------------------------------------------END------------------------------------------------------------------