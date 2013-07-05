

//Begin boilerplate needed to make django's csrf protection play nice with AJAX

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
function sameOrigin(url) {
    // test that a given url is a same-origin URL
    // url could be relative or scheme relative or absolute
    var host = document.location.host; // host + port
    var protocol = document.location.protocol;
    var sr_origin = '//' + host;
    var origin = protocol + sr_origin;
    // Allow absolute or scheme relative URLs to same origin
    return (url == origin || url.slice(0, origin.length + 1) == origin + '/') ||
        (url == sr_origin || url.slice(0, sr_origin.length + 1) == sr_origin + '/') ||
        // or any other URL that isn't scheme relative or absolute i.e relative.
        !(/^(\/\/|http:|https:).*/.test(url));
}

$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
            // Send the token to same-origin, relative URLs only.
            // Send the token only if the method warrants CSRF protection
            // Using the CSRFToken value acquired earlier
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});

//End AJAX csrf boilerplate

var map;
var borders;
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
        $.post("query",{lat: lat_, lng: lng_},
            function(data) {
                geojson_data = $.parseJSON(data);
                borders = new GeoJSON(geojson_data);
                for(var i = 0; i < borders.length; ++i) {
                    var border = borders[i];
                    border.setMap(map);
                }
            }
        )
    });
}
