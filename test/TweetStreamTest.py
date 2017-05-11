import tweepy
from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import json
 
consumer_key = 'AcDWcG2mvzd2fnxl7cW87DftK'
consumer_secret = 'Z91dGxpxzrXtZSivhVZXoZt5wxqpwXRcS0L6E0vncmTCfofvMK'
access_token = '852447886079959040-B79JXJ3I7I5WS5I8ReCBse26JiTKhjs'
access_secret = 'bKToLr7NDe9NtXjmJ1aka7UcGdDJB4YNwUakwNN3seICS'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)

'''
for friend in tweepy.Cursor(api.friends).items(10):
    # Process a single status
    print(friend._json)
'''

 
class MyListener(StreamListener):
 
    def on_data(self, data):
        try:
            with open('python.json', 'a') as f:
                f.write(data)
                return True
        except BaseException as e:
            print("Error on_data: %s"%str(e))
        return True
 
    def on_error(self, status):
        print(status)
        return True
 
twitter_stream = Stream(auth, MyListener())
twitter_stream.filter(track=['#python'])