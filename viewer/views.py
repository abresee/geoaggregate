from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.gis.geos import Point
from django.template import RequestContext
from .models import WorldBorder
import json

def index(request):
    'Just a Map, yo'
    return render_to_response('viewer/index.html',
        context_instance=RequestContext(request))

def query(request):
    get = request.GET
    point = Point(float(get['lng']),float(get['lat']))
    qs = WorldBorder.objects.filter(geom__contains=point)
    qs.geojson()
    results={}
    for border in qs:
        results[border.name] = "__{}__".format(border.name)
    resultsJSON=json.dumps(results)
    for border in qs:
        resultsJSON=resultsJSON.replace('"__{}__"'.format(border.name),border.geom.geojson)
    return HttpResponse(resultsJSON) 
