from flask import Flask,request,make_response
import urllib
from geojson import Feature, Point, FeatureCollection
import couchdb
import json
import geojson

app = Flask(__name__)

@app.route('/')
def form():
    #var = urllib.request.urlopen("https://wanderdrone.appspot.com/").read()
    #var = var.decode("utf-8")
    
    #print (type(var))

    f = open("testGeoJson.geojson", encoding='utf-8')
    geoJSON = geojson.load(f)

    #rst = make_response(var)
    rst = make_response(str(geoJSON))  
    rst.headers['Access-Control-Allow-Origin'] = '*'
    # a = {"geometry": {"type": "Point", "coordinates": [132.63686443893161, -27.190744312165926]}, "type": "Feature", "properties": {}}
    # data = json.dumps(a)
    # print (type(data))
    print (rst)
    return rst


if __name__ == '__main__':
  app.run(
        host="",
        port=1337
  )