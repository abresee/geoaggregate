$ = jQuery
$(document).ready ->
    map = new google.maps.Map document.getElementById('map-canvas'),
        zoom: 3
        center: new google.maps.LatLng(42.358431, -71.059773),
        mapTypeId: google.maps.MapTypeId.SATELLITE

    $('#go').click ->
        $.get 'demo', (data) ->
            p = $.parseJSON data
            latlng = new google.maps.LatLng p.lat, p.lon
            map.panTo latlng
            report = "Land: #{p.land_area}<br>" +
                "Water: #{p.water_area}<br>" +
                "Total: #{p.land_area + p.water_area}"
            borders = new GeoJSON p.geom
            border = borders[0]
            border.setMap(map)
            map.setZoom(9)
            
            $("#report").append(report)
