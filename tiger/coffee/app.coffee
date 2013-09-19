$ = jQuery
$(document).ready ->
    map = new google.maps.Map document.getElementById('map-canvas'),
        zoom: 3
        center: new google.maps.LatLng(42.358431, -71.059773),
        mapTypeId: google.maps.MapTypeId.SATELLITE
    $('#go').button().click ->
        #state = $('#state').val()
        #county = $('#county').val()       
        state = 'Texas'
        county = 'Travis'
        url = "demo/#{state}/#{county}"
        $.get url, (data) ->
            p = $.parseJSON data
            report = "Land area: #{p.area.l} sq feet<br>" +
                "percentile: #{p.area_p.l}%<br>" + 
                "Water area: #{p.area.w} sq feet<br>" +
                "percentile: #{p.area_p.w}%<br>" + 
                "Total: #{p.area.t} sq feet<br>" +
                "percentile: #{p.area_p.t}%<br>"  

            sw = new google.maps.LatLng p.extent[1], p.extent[0]
            ne = new google.maps.LatLng p.extent[3], p.extent[2]
            bounds = new google.maps.LatLngBounds sw, ne
            
            map.fitBounds bounds

            borders = new GeoJSON p.geom
            border = borders[0]
            border.setMap map
            
            $("#report").append report 
            return
        return
    return

