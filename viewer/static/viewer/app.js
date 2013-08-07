var map;
var borders=[];
var geojson_data;
function initialize() {
    map = new google.maps.Map(document.getElementById('map-canvas'),
        {
            zoom: 3,
            center: new google.maps.LatLng(42.358431, -71.059773),
            mapTypeId: google.maps.MapTypeId.SATELLITE
        });

    google.maps.event.addListener(map, 'click', function(event) {
        lat_ = event.latLng.lat();
        lng_ = event.latLng.lng();
        $.get("query",{lat: lat_, lng: lng_},
            function(data) {
                parsed_data = $.parseJSON(data);
                $.each(parsed_data, function(key,value) {
                    $("#report").append(key+"<br>");
                    var new_borders = new GeoJSON(value);
                    for(var i = 0; i < new_borders.length; ++i) {
                        var border = new_borders[i];
                        border.setMap(map);
                    }
                });
            }
        )
    });

    $("#ajax_render_test").click(function() {
        $.get("ajax_render_test",
            function(data) {
                $("#report").append(data);
            }
        );
    });
}
