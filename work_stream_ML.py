import tweepy
import json
import os
import indicoio


# Authentication details for twitter and indicoio
consumer_key = 'eimcELjV8NV1Uor5OtKX7BMYd'
consumer_secret = 'YSgbJ4u4Hz669EG4J87od4NGIJtKIMwYUX0zjuRl6WyTo52EJu'
access_token = '845462705863610370-EYNCrVXZd2CYgyysQUCywm7W1MlcN7Z'
access_token_secret = 'agYyRPjwGgfMVEwtT3E7EWI5qYhln8jBZJ1H3S5jzZcYS'
indicoio.config.api_key = 'bf7b2ed0991819389f48384b97b61d58'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

# This is the listener, resposible for receiving data
class StdOutListener(tweepy.StreamListener):
    def on_data(self, data):
        
        
        # Twitter returns data in JSON format - we need to decode it first
        decoded = json.loads(data)
        tweetString= decoded['text'].replace("@birdsongbot","").replace("\n","")

        # Also, we convert UTF-8 to ASCII ignoring all bad characters sent by users
        os.system("say {0}".format(tweetString))
        print(tweetString)
        print('')
        
        #INDICO SENTIMENT JAZZ
        sentimentVal = indicoio.sentiment(tweetString)
        print(sentimentVal)
        sentimentVal = int(sentimentVal * 5 + 1)
        print(sentimentVal)
        
        
        
        
        
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    print("Showing all new tweets for @birdsongbot:")

    # There are different kinds of streams: public stream, user stream, multi-user streams
    # In this example follow #programming tag
    # For more details refer to https://dev.twitter.com/docs/streaming-apis
    stream = tweepy.Stream(auth, l)
    stream.filter(track=['@birdsongbot'])