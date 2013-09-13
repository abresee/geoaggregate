from django.http import HttpResponse
from django.shortcuts import render_to_response
from tiger.models import County, State
import json

def index(request):
    return render_to_response('tiger/index.html')

def demo(request,county,state):
    
    state_f = State.objects.get(name=state).fips
    c = County.objects.get(name=county,state_fips=state_f)
    geom = c.geom.geojson

    l_area = c.land_area
    w_area = c.water_area
    t_area = l_area + w_area


    results = {
        'lat': c.lat, 
        'lon' : c.lon,
        'land_area' : l_area, 
        'water_area' : w_area,
        'geom' : '__geom__'
    }
    resultsJSON = json.dumps(results)
    resultsJSON = resultsJSON.replace('"__geom__"',geom)

    return HttpResponse(resultsJSON)
    
    
    

