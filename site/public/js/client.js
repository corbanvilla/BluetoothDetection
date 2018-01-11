//Google Maps - DO NOT TOUCH
var markers = [];

function initMap() {
        var city = {lat: 40.296898, lng: -111.694647};
        var place = {lat: null,lng: null}

        // Create a map object and specify the DOM element for display.
        var map = new google.maps.Map(document.getElementById('map'), {
          center: city,
          zoom: 15
        });

        //Ajax
        $.get("database", function(data, status){
            (function drop() {
              for (var i = 0; i < data.length; i++) {
                addMarker(data[i].latitude, data[i].longitude, i * 400);
              }
          }) ();

        });

        function addMarker(latitude, longitude, timeout) {
            window.setTimeout(function() {
                markers.push(new google.maps.Marker({
                    position: {lat: latitude, lng: longitude},
                    map: map,
                    animation: google.maps.Animation.DROP
                }));
            }, timeout);
        }
}
