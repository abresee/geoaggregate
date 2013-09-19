# coffeescript rewrite of Jason Sanford's GeoJSON-to-Google-Maps 
# https://github.com/JasonSanford/GeoJSON-to-Google-Maps.git

_make_latlng = (coord) ->
    new google.maps.LatLng coord[1], coord[0]

_make_point = (coord, opts, props) ->
    opts.position = _make_latlng coord
    r = new google.maps.Marker opts
    if props then r.set "geojsonProperties", props
    return r

_make_linestring = (coords, opts, props) ->
    opts.path = [_make_latlng(coord) for coord in coords]
    r = new google.maps.Polyline opts
    if props then r.set "geojsonProperties", props
    return r

_make_multipoint = (coords, opts, props) ->
    [_make_point(coord, opts, props) for coord in coords]

_make_multilinestring = (coords, opts, props) ->
    [_make_linestring(coord, opts, props) for coord in coords]

_make_path = (line) ->
    [_make_latlng(coord) for coord in line]

_make_polygon = (coords, opts, props) ->
    paths = []

    ext_path = _make_path coords[0]
    ext_dir = _ccw ext_path
    paths.push ext_path

    if coords.length > 1
        int_path = _make_path coords[1]
        int_dir = _ccw int_path
        flip = ext_dir == int_dir

        if flip 
            paths.push int_path.reverse()
        else
            paths.push int_path

        if coords.length > 2
            for line in coords[2..]
                path = _make_path(line)

                if flip
                    paths.push path.reverse()
                else
                    paths.push path

    opts.paths = paths
    r = new google.maps.Polygon opts
    if props then r.set "geojsonProperties", props
    return r

_make_multipolygon = (coords, opts, props) ->
    [_make_polygon(coord, opts, props) for coord in coords]

_make_geometrycollection = (geoms, opts, props) ->
    [_geom_to_gmaps geom, opts, props for geom in geoms]

_geom_to_gmaps = ( geom, opts, props ) ->
    
    r = null
    coords = geom.coordinates
    
    switch geojsonGeometry.type
        when "Point"
            r = _make_point coords, opts, props

        when "MultiPoint"
            r = _make_multipoint coords, opts, props

        when "LineString"
            r = _make_linestring coords, opts, props 

        when "MultiLineString"
            r = _make_multilinestring coords, opts, props

        when "Polygon"
            r = _make_polygon coords, opts, props

        when "MultiPolygon"
            r = _make_multipolygon coords, opts, props

        when "GeometryCollection"
            r = _make_geometrycollection coords, opts, props

        else
            googleObj = _error()

    return r

_error = () ->
    {type: "Error", message: "well, shit's broke. did you validate your shit?"}

_ccw = (path) ->
    a = 0
    for i in [0..path.length-2] by 1
        a += ( # I'm pretty sure the below is finding the determinant
            ((path[i+1].lat() - path[i].lat()) * (path[i+2].lng() - path[i].lng())) - (path[i+2].lat() - path[i].lat()) * (path[i+1].lng() - path[i].lng())
        )
    return a > 0

_make_featurecollection = (feats) ->
    feats = geojson.features
    [_geom_to_gmaps(feat.geometry, opts, feat.properties) for feat in feats]

GeoJSON = (geojson, options ) ->
    opts = options or {}
    r = null
    switch geojson.type
        when "FeatureCollection"
            feats = geojson.features
            r = _make_featurecollection feats, opts, feats.properties

        when "GeometryCollection"
            geoms = geojson.geometries
            r = _make_geometrycollection geoms, opts, geoms.properties

        when "Feature"
            r = _geom_to_gmaps geojson.geometry, opts, geojson.properties

        when "Point", "MultiPoint", "LineString", "MultiLineString", "Polygon", "MultiPolygon"
            r = _geometryToGoogleMaps(geojson, opts)

        else
            r = _error()
    return r
