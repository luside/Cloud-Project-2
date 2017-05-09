from flask import Flask,request,make_response
import urllib
from geojson import Feature, Point, FeatureCollection
import couchdb
import json
import geojson

app = Flask(__name__)
server = couchdb.Server('http://115.146.92.189:5984/')
db = server['testing']

map_fun = '''function(doc) {
    var doctime=new Date(doc.time);
    var docminute=doctime.getMinutes();
    var docsecond=doctime.getSeconds();
    var currenttime=new Date();
    var currentminute=currenttime.getMinutes();
    var currentsecond=currenttime.getSeconds();
    if(currentminute>docminute){
        var diff=(currentminute-docminute)*60+(currentsecond-docsecond);
}
    if(currentminute==docminute){
        var diff=currentsecond-docsecond;
}
 
    if(diff<-10)
        emit({"coordinate":doc.location,"score":doc.score},diff);
}'''

@app.route('/')
def form():
    #var = urllib.request.urlopen("https://wanderdrone.appspot.com/").read()
    #var = var.decode("utf-8")
    # f = open("testGeoJson.geojson", encoding='utf-8')
    # geoJSON = geojson.load(f)

    features = []
    for row in db.query(map_fun):
        geoData = row.key
        geoData['coordinate'].reverse()
        features.append(Feature(geometry=Point(geoData['coordinate']),properties={'score':geoData['score']}))
        #row.value

    featureCollection = FeatureCollection(features)

    print(len(features))
    #rst = make_response(var)
    rst = make_response(str(featureCollection))  
    rst.headers['Access-Control-Allow-Origin'] = '*'
    # a = {"geometry": {"type": "Point", "coordinates": [132.63686443893161, -27.190744312165926]}, "type": "Feature", "properties": {}}
    # data = json.dumps(a)
    # print (type(data))
    print (rst)
    return rst



@app.route('/hello', methods=['POST'])
def hello():
    name=request.form['yourname']
    return "Welcome, " + name +'\n'


if __name__ == '__main__':
  app.run(
        host="",
        port=1337
  )