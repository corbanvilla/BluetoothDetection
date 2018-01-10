/*
var data = [{"field":"Data","type":"date"},  {"field":"Numero","type":"number"}];

var columns = {};

var index = 0;

$.each(data, function() {

    columns[index] = {
        field : this.field,
        type : this.type
    };

    index++;
});

console.log(columns);
//console.log(columns.field)
*/

//Google Maps - DO NOT TOUCH
var options = {
   host: 'vpn.unicornsforlife.com',
   port: '8080',
   path: '/index.htm'
};

function initMap() {
        var city = {lat: 40.296898, lng: -111.694647};
        var place = {lat: null,lng: null}

        // Create a map object and specify the DOM element for display.
        var map = new google.maps.Map(document.getElementById('map'), {
          center: city,
          zoom: 12
        });

        // Create a marker and set its position.
        var marker = new google.maps.Marker({
          map: map,
          position: city,
          title: 'Hello World!'
        });
      }

//Ajax
$(document).ready(function(){
    $("button").click(function(){
        $.get("database", function(data, status){
            console.log(data);
            console.log("calling func storeAjax")
            storeAjax(JSON.parse(data));
        });
    });

});

function storeAjax(data){
    var columns = {};
    var index = 0;
    $.each(data, function() {
        columns[index] = {
            name : this.name,
            vendor: this.vendor,
            first_seen: this.first_seen,
            last_seen: this.last_seen
        };
        index++;
    });
    console.log(columns);
    console.log(columns[0].uuid);
}
