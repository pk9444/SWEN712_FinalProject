'''
SWEN 712 - Engineering Accessible Software- Final Project Deliverable

@developed by: Sai Gowtham Kapa, Vaibhavi Raut, Manish Hemkant Waghdhare, Pratyush Karna

@Interpreter- 3.6.0

This is a python script that allows a user to input a twitter user account and retrieve the top 5 Hashtags (#) for a
range of latest tweets also input by the user.
'''

#Import tweepy library to read load tweets into the input
import tweepy
from tweepy import OAuthHandler, StreamListener
#OAuthHandler- handles key authentication
#StreamListener- takes the input tweets (from a range of tweets) in the form of a stream

#------------------------------------------------START------------------------------------------------------------------

#Main Class
class TopHashtags(StreamListener):
    '''
    Override Stream Listener Function on_data() to print a data stream
    '''
    def on_data(self, data):
        print(data)
        return True

    '''
    Override Stream Listener Function on_error() to return error is reading a stream (tweet) if any
    '''
    def on_error(self, status):
        print(status)


'''
    Driver Function
    '''
def main():
        global api

        #read the public keys and tokens and secret keys and tokens generated from Twitter Dev Portal

        consumer_key = 's3r7ur5Me5sLf52UoikNnTxTU'
        consumer_secret = 'YywlePc0PwnPjmHtPIWLbb3bbEWWGUd9ZMAtBGnDjCO4UPVpWk'
        access_token = '1227789853720444928-znowOuipGqmVZG0g1bUTm3JRUzZDPB'
        access_token_secret = 'hWkGZ84fOy8oNGfxDL3Z96lJkKxnslkQf8rzMKv3EEhBw'

        #initialize an empty hashtag dictionary
        hashtags_dictionary = {}

        '''
        try-except block to handle the authentication provided by the OAuthHandler interface of tweepy
        @:exception - Checked Exception for failed Authentication 
        '''
        try:
         auth = OAuthHandler(consumer_key, consumer_secret)
         auth.set_access_token(access_token, access_token_secret)
         api = tweepy.API(auth)

        except:
         print("Authentication failed...")

       #Taking user inputs
        user_name = input("Enter Twitter User Account without @: \n")
        num_tweets = input("Enter no. of latest tweets to process:  \n")


        #getting the total Tweets from the user name and its range
        tweets = api.user_timeline(screen_name=user_name, count=num_tweets)

        #Iterating through the tweets and getting Hashtags
        for tweet in tweets:
            hashtags = tweet.entities.get('hashtags') #function tp gets hashtags using StreamListener
            for hashtag in hashtags: #Running a nested loop for search for hashtags within the tweets
                if hashtag['text'] in hashtags_dictionary.keys(): #if present in the dictionary then add 1 else don't
                    hashtags_dictionary[hashtag['text']] += 1
                else:
                    hashtags_dictionary[hashtag['text']] = 1
        print("The top 5 # for the account " + user_name + "from the latest " + num_tweets + " are: ")
        print(sorted(hashtags_dictionary, key=hashtags_dictionary.get, reverse=True)[:5])
        print("\n")


# Calling main function
if __name__ == "__main__":
     while(True):
      main()

#--------------------------------------------------END------------------------------------------------------------------