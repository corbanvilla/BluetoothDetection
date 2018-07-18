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
                addMarker(data[i].name, data[i].latitude, data[i].longitude, i * 400, i,
                    data[i].vendor, data[i].first_seen, data[i].last_seen, data[i].threat_rating);
              }
          }) ();
        });

        function addMarker(title, latitude, longitude, timeout, i, vendor, first_seen, last_seen, rating) {
            window.setTimeout(function() {
                markers.push(new google.maps.Marker({
                    position: {lat: latitude, lng: longitude},
                    map: map,
                    animation: google.maps.Animation.DROP,
                    title: title
                }));
                contentString = customContent(title, vendor, first_seen, last_seen, rating);
                function customContent(title, vendor, first_seen, last_seen, rating) {
                    var contentString = '<div id="content">' +
                        '<h1 id="firstHeading" class="firstHeading">' + 'Device Name: ' + title + '</h1>' +
                        '<div id="bodyContent">'+
                        '<p>' + 'Vendor: ' + vendor + '</p>'+
                        '<p>' + 'First Seen: ' + first_seen + '</p>'+
                        '<p>' + 'Last Seen: ' + last_seen + '</p>'+
                        '<p>' + 'Threat Rating: ' + rating + '</p>'+
                        '<p>' + 'Reason: ' + //added in future
                        '</div>';
                        return (contentString);
                    }

                var infowindow = new google.maps.InfoWindow({
                    content: contentString
                });

                console.log(markers[i]);
                markers[i].addListener('click', function() {
                    infowindow.open(map, markers[i]);
                });
            }, timeout);

        }
}
