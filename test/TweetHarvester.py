#Author:Side Lu<sidel@student.unimelb.edu.au>
#Date: 10/5/2017
#Project:COMP90024 Cluster and Cloud Computing Assignment2
#We use REST API provided by Twitter to access data
from tweepy import StreamListener
import json, time, sys
from textblob import TextBlob
import couchdb
from tweepy import OAuthHandler
import tweepy

class SListener(StreamListener):

    #initialize the listener
    #we initialize with two database address.One for storage, the other for presentation
    def __init__(self, api = None, fprefix = 'streamer',db_address_1 = 'http://115.146.95.85:5984/',db_address_2 = 'http://115.146.92.189:5984/'):
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.server_1 = couchdb.Server(db_address_1)
        self.server_2 = couchdb.Server(db_address_2)


    def on_data(self, data):
        
        #after getting the twitter data, we store attributes that we want into databases
        #and ignore data without coordinates information
        if 'in_reply_to_status' in data:
            try:
                var = json.loads(data)
                dict = {}
                dict["id"] = var["id"]
                dict["content"] = var["text"]
                dict["time"] = var["created_at"]
                dict["location"] = var["coordinates"]["coordinates"]
                dict["score"] = TextBlob(var["text"]).sentiment.polarity
                print ("One tweet -> " + str(dict))
                db_1 = self.server_1['python-tests']
                db_2 = self.server_2['testing']
                db_1.save(dict)
                db_2.save(dict)
                print("success saving! " + str(dict["id"]))
                return dict
            except Exception as ex:
                print (str(ex))



            # self.on_status(data)
        elif 'delete' in data:
            delete = json.loads(data)['delete']['status']
            if self.on_delete(delete['id'], delete['user_id']) is False:
                return False
        elif 'limit' in data:
            if self.on_limit(json.loads(data)['limit']['track']) is False:
                return False
        elif 'warning' in data:
            warning = json.loads(data)['warnings']
            print(warning['message'])
            return False

    def on_status(self, status):
        return

    def on_delete(self, status_id, user_id):
        return

    def on_limit(self, track):
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return

# token
consumer_key='<your consumer key>'
consumer_secret = '<your consumer secret>'
access_token='<your access token>'
access_secret='<your access secret>'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def main():
    # the locations shows the area from which we want to get twitter data
    #here we draw a bounding box of Australia on AURIN 
    locations = [112.5927, -44.2745, 153.1982, -10.1492]
    #initialize the listener
    listen = SListener(api, 'Australia')
    #use stream to get twitter data
    stream = tweepy.Stream(auth, listen)

    print("Streaming started...")

    try:
        #get twitter in our specific area
        stream.filter(locations=locations)

    except Exception as ex:
        #handle exception
        print(str(ex))
        print("error!")
        # stream.disconnect()


if __name__ == '__main__':
    main()
