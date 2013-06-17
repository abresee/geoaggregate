var map;

function initialize() {
    map = new google.maps.Map(document.getElementById('map'),
        {
            zoom: 5,
            center: new google.maps.LatLng(42.358431, -71.059773),
            mapTypeId: google.maps.MapTypeId.ROADMAP
        });

    google.maps.event.addListener(map, "rightclick", function(event) {
        var lat = event.latLng.lat();
        var lng = event.latLng.lng();
        // populate yor box/field with lat, lng
        alert("Lat=" + lat + "; Lng=" + lng);
    });
}


$(document).ready(function() {
});
