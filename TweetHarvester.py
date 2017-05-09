from tweepy import StreamListener
import json, time, sys
from textblob import TextBlob
import couchdb
from tweepy import OAuthHandler
import tweepy

class SListener(StreamListener):

    def __init__(self, api = None, fprefix = 'streamer',db_address_1 = 'http://115.146.95.85:5984/',db_address_2 = 'http://115.146.92.189:5984/'):
        self.api = api
        self.counter = 0
        self.fprefix = fprefix
        self.server_1 = couchdb.Server(db_address_1)
        self.server_2 = couchdb.Server(db_address_2)


    def on_data(self, data):

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
        # self.output.write(status + "\n")
        #
        # self.counter += 1
        #
        # if self.counter >= 20000:
        #     self.output.close()
        #     self.output = open(self.fprefix + '.'
        #                        + time.strftime('%Y%m%d-%H%M%S') + '.json', 'w')
        #     self.counter = 0
        return

    def on_delete(self, status_id, user_id):
        # self.delout.write( str(status_id) + "\n")
        return

    def on_limit(self, track):
        # sys.stderr.write(track + "\n")
        return

    def on_error(self, status_code):
        sys.stderr.write('Error: ' + str(status_code) + "\n")
        return False

    def on_timeout(self):
        sys.stderr.write("Timeout, sleeping for 60 seconds...\n")
        time.sleep(60)
        return
#Junyuan's token
''' consumer_key = '5XF7i5eVvSHmaYvwk9pXm1aTW'
consumer_secret = 'FYSiNwJ2n3hhK0zhML3kTv5MIzWQQmb1sY2QFcC4HPCRQhO3Bl'
access_token = '702844657135329280-qkWhN7FyStxJH2Qq1HVjIFpH3Hr8O5K'
access_secret = 'HVvRCPK1leCG8IyLl2eJ5jR5ZZfJNVhPWrKRaPj53EyU7' '''

#Liam's token
'''consumer_key = 'ibL3HDH2s2e3JNN2wkL3rgzsT'
consumer_secret = 'Gq51qoHwRAjWpjUTQ5IWFj2exCcvMtmiCIZahtpJ3IHSe3Vzcv'
access_token = '852463386700922880-9ll4KX0DNAGKpC3hgTPcSCFgHdXmULF'
access_secret = 'pbewWtBcpljilaYiRcD229YJZyeuW7nOkOqwWqO5dxa0X' '''

#Side's token
consumer_key='8PNF7aMlERZFxs6qYlowHLSQe'
consumer_secret = 'qP0KKhVpLkXlO4wJdKHKwZJfDDruFLpSBeIKlueZWIoaAl4EX9'
access_token='852460734524964869-D3kZYGXzZ7xB2hIpv1G8p6NGndiqnTH'
access_secret='P0MfyHNL6quP4SRMQU0JmCCh7x4VIBQzud2Qa0OiswPok'


auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)


def main():
    # track = ["location","Australia"]
    locations = [112.5927, -44.2745, 153.1982, -10.1492]

    listen = SListener(api, 'Australia')
    stream = tweepy.Stream(auth, listen)

    print("Streaming started...")

    try:
        stream.filter(locations=locations)

    except Exception as ex:
        print(str(ex))
        print("error!")
        # stream.disconnect()


if __name__ == '__main__':
    main()