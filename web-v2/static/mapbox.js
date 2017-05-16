//token of mapbox
mapboxgl.accessToken = '<your mapbox token>';

//the url of flask server, use it to get realtime geo data of tweets from couchDB
//change the port 1337 if it is being used by another application
var url = 'http://localhost:1337/data/';

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
                    duration: 3000      //fadeIn/fadeOut time
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
        },7000);    //wait time begore fadeOut, that is, display time

        //after waitting 5 seconds and fadeOut in 2 seconds (7 seconds totally), remove source for the points
        window.setTimeout(function() {
            map.removeLayer(layerId);
            map.removeSource(pointId);
        },10000);
        
    }, 3000);   //interval time of query new points
});

var isAtStart = true;

document.getElementById('fly_to_sydney').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [151.134491,-33.874600] : [151.134491,-33.874600];

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

document.getElementById('fly_to_melbourne').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [144.963988,-37.797722] : [144.963988,-37.797722];

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

document.getElementById('fly_to_center').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [125., -27]: [125, -27];

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 3.8,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1.5, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

document.getElementById('fly_to_brisbane').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [153.015405,-27.465959] : [153.015405,-27.465959];

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1.5, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

document.getElementById('fly_to_perth').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [115.851846,-31.942477] : [115.851846,-31.942477] ;

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1.5, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

document.getElementById('fly_to_canberra').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [149.129049,-35.281922] : [149.129049,-35.281922] ;

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1.5, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});


document.getElementById('fly_to_adelaide').addEventListener('click', function() {
    // depending on whether we're currently at point a or b, aim for
    // point a or b
    var target = isAtStart ? [138.595829,-34.921451] : [138.595829,-34.921451] ;

    // and now we're at the opposite point
    isAtStart = !isAtStart;

    map.flyTo({
        // These options control the ending camera position: centered at
        // the target, at zoom level 9, and north up.
        center: target,
        zoom: 10,
        bearing: 0,

        // These options control the flight curve, making it move
        // slowly and zoom out almost completely before starting
        // to pan.
        speed: 1.6, // make the flying slow
        curve: 1.5, // change the speed at which it zooms out

        // This can be any easing function: it takes a number between
        // 0 and 1 and returns another number between 0 and 1.
        easing: function (t) {
            return t;
        }
    });
});

//map.addControl(new mapboxgl.FullscreenControl());
