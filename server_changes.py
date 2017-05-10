from flask import Flask,request,make_response
import urllib
from geojson import Feature, Point, FeatureCollection
import couchdb
import json
import geojson

app = Flask(__name__)
server = couchdb.Server('http://115.146.92.189:5984/')
db = server['testing']

the_var = db.changes(
    descending=True,
    limit=1
)
index = [the_var['results'][-1]['seq']]

@app.route('/')
def form():
    #var = urllib.request.urlopen("https://wanderdrone.appspot.com/").read()
    #var = var.decode("utf-8")
    # f = open("testGeoJson.geojson", encoding='utf-8')
    # geoJSON = geojson.load

    print("-->> start from ", index[0])


    data = db.changes(
        since=index[0])

    last_index = db.changes(
        descending=True,
        limit=1
    )
    index[0] = last_index['results'][-1]['seq']

    print("-->> index for next round ", index[0])

    features = []
    var_list = []
    for each in data['results']:
        var_list.append(db[each['id']])

    for each in var_list:
        emotion = ""
        if each['score'] > 0.0:
            emotion = "positive"
        elif each['score'] < 0.0:
            emotion = "nagtive"
        else:
            emotion = "neutral"
        features.append(Feature(geometry=Point(each['location']),properties={'score':emotion}))

    featureCollection = FeatureCollection(features)

    rst = make_response(str(featureCollection))  
    rst.headers['Access-Control-Allow-Origin'] = '*'

    return rst


if __name__ == '__main__':
  app.run(
        host="",
        port=1337
  )