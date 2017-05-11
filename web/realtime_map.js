//token of mapbox
mapboxgl.accessToken = 'pk.eyJ1IjoibGl1anVueXVhbiIsImEiOiJjajJlbDN5dTYwNmRoMzJvODhscTZ3bnFkIn0.Vhoj1WBop0EnuGKlTm6I2w';

//the url of flask server, use it to get realtime geo data of tweets from couchDB
//change the port 1337 if it is being used by another application
var url = 'http://localhost:1337/';

//create a new map
var map = new mapboxgl.Map({
    container: 'map',
    style: 'mapbox://styles/mapbox/dark-v9',
    center: [125, -27],   //the center of australia
    zoom: 4
});

var count = 0;   //use count to create an unique id for each source and layer
map.on('load', function () {
    window.setInterval(function() {
        count++;
        var pointId = 'geo_points_'+count;
        var layerId = 'point_layer_'+count;
        map.addSource(pointId, {type: 'geojson', data: url});
        map.addLayer({
            "id": layerId,
            "source": pointId,
            "type": "circle",
            "paint": {
                "circle-radius": {
                    'base': 4,
                    'stops': [[3.7, 4], [11, 10]]
                },
                "circle-opacity": 0,
                "circle-opacity-transition": {
                    duration: 2000      //fadeIn/fadeOut time
                },
                "circle-color": {
                    property:"score",
                    type: "categorical",
                    stops: [
                        ["positive","#A94A42"],
                        ["neutral","#CAA038"],
                        ["negative","#7DBC99"]
                    ]
                }
            }
        });
        //show the points by setting 'circle-opacity' to 1
        window.setTimeout(function() {
            map.setPaintProperty(layerId, 'circle-opacity', 1);
        },1);
        //wait 5 seconds, then let the points fade out
        window.setTimeout(function() {
            map.setPaintProperty(layerId, 'circle-opacity', 0);
        },5000);    //wait time begore fadeOut, that is, display time

        //after waitting 5 seconds and fadeOut in 2 seconds (7 seconds totally), remove source for the points
        window.setTimeout(function() {
            map.removeLayer(layerId);
            map.removeSource(pointId);
        },7000);
        
    }, 5000);   //interval time of query new points
});
