var map;

function initialize() {
    map = new google.maps.Map(document.getElementById('map'),
        {
            zoom: 15,
            center: new google.maps.LatLng(42.358431, -71.059773),
            mapTypeId: google.maps.MapTypeId.SATELLITE
        });

    google.maps.event.addListener(map, 'click', function(event) {
        placeMarker(event.latLng);
      });
}

function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
})}


$(document).ready(function() {
});
