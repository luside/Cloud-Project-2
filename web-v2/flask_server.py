from flask import Flask,request,make_response, render_template, url_for
from geojson import Feature, Point, FeatureCollection
import couchdb
import json

#create a flask server
app = Flask(__name__)
# app.url_for('static', filename='echart1.js')
# app.url_for('static', filename='echart2.js')
# app.url_for('static', filename='realtime_map.js')

#connect couchDB
server = couchdb.Server('<your couchDB address>')
db = server['<your chouchDB name>']

#get the latest change of the couchDB
the_var = db.changes(
    descending=True,
    limit=1
)
#get the latest seq number from latest change
index = [the_var['results'][-1]['seq']]

#get latest tweets 
@app.route('/data/')
def form():

    print("-->> start from ", index[0])
    #get the latest change from latest seq
    data = db.changes(
        since=index[0])

    last_index = db.changes(
        descending=True,
        limit=1
    )
    #update latest seq number
    index[0] = last_index['results'][-1]['seq']

    print("-->> index for next round ", index[0])
    #get the latesd tweets via seq
    var_list = []
    for each in data['results']:
        var_list.append(db[each['id']])
    
    features = []
    for each in var_list:
        #classify the emotion type of the tweet
        emotion = ""
        if each['score'] > 0.0:
            emotion = "positive"
        elif each['score'] < 0.0:
            emotion = "negative"
        else:
            emotion = "neutral"

        #encode the data in geoJSON feature format
        features.append(Feature(geometry=Point(each['location']),properties={'score':emotion}))
    
    #collect featues
    featureCollection = FeatureCollection(features)
    
    # allow cross-domain access
    rst = make_response(str(featureCollection))  
    rst.headers['Access-Control-Allow-Origin'] = '*'

    return rst

@app.route('/')
def indexpage():
    webpage = render_template('index.html')
    return webpage


#run the server, change the port if it isused by another application
if __name__ == '__main__':
    app.run(
        host="",
        port=1337
  )
