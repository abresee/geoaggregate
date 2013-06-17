var map;

function initialize() {
    map = new google.maps.Map(document.getElementById('map'),
        {
            zoom: 3,
            center: new google.maps.LatLng(42.358431, -71.059773),
            mapTypeId: google.maps.MapTypeId.SATELLITE
        });

    google.maps.event.addListener(map, 'click', function(event) {
        lat_ = event.latLng.lat();
        lng_ = event.latLng.lng();
        $.post("query",{lat: lat_, lng: lng_},
            function(data) {
                $("#result").text(data)
            }
        )
    });
}

function placeMarker(location) {
    var marker = new google.maps.Marker({
        position: location,
        map: map
})}


$(document).ready(function() {
});
