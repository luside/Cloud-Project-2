
from tweepy import OAuthHandler
from slistener import SListener
import time, tweepy, sys

consumer_key = '<your consumer key>'
consumer_secret = '<your consumer secret>'
access_token = '<your access token>'
access_secret = '<your access secret>'

auth = OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

def main():
    #track = ["location","Australia"]
    locations=[112.5927,-44.2745,153.1982,-10.1492]
 
    listen = SListener(api, 'Australia')
    stream = tweepy.Stream(auth, listen)

    print("Streaming started...")

    try: 
        stream.filter(locations=locations)
    except:
        print ("error!")
        stream.disconnect()

if __name__ == '__main__':
    main()
