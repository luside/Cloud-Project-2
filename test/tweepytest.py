
from tweepy import OAuthHandler
from slistener import SListener
import time, tweepy, sys

consumer_key = '8PNF7aMlERZFxs6qYlowHLSQe'
consumer_secret = 'qP0KKhVpLkXlO4wJdKHKwZJfDDruFLpSBeIKlueZWIoaAl4EX9'
access_token = '852460734524964869-D3kZYGXzZ7xB2hIpv1G8p6NGndiqnTH'
access_secret = 'P0MfyHNL6quP4SRMQU0JmCCh7x4VIBQzud2Qa0OiswPok'

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
