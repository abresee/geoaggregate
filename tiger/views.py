from django.http import HttpResponse
from django.shortcuts import render_to_response
from tiger.models import County, State
from scipy import stats
import json

def index(request):
    return render_to_response('tiger/index.html')

def demo(request,county,state):
    
    state_f = State.objects.get(name=state).fips
    c = County.objects.get(name=county,state_fips=state_f)

    geom = c.geom.json
    center = c.geom.centroid.json
    extent = c.geom.extent

    area = {
        'l' : c.land_area,
        'w' : c.water_area,
        't' : c.land_area + c.water_area,
    }

    q = County.objects.filter(state_fips=state_f)
    areas = {
        'l' : [i.land_area for i in q],
        'w' : [i.water_area for i in q],
        't' : [i.land_area + i.water_area for i in q]
    }

    area_p = { 
            k : "{:.2f}".format(
                stats.percentileofscore(areas[k], area[k]))
            for k in area.keys()
    }

    results = {
        'lat': c.lat, 
        'lon' : c.lon,
        'area' : area, 
        'area_p' : area_p,
        'geom' : '__geom__',
        'center' : '__center__',
        'extent' : extent
    }
    resultsJSON = json.dumps(results)
    resultsJSON = resultsJSON.replace('"__geom__"', geom)
    resultsJSON = resultsJSON.replace('"__center__"', center)

    return HttpResponse(resultsJSON)
    
    
    

