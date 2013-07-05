from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.gis.geos import Point
from django.template import RequestContext
from .models import WorldBorder
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    'Just a Map, yo'
    return render_to_response('test_query/index.html',
        context_instance=RequestContext(request))

@csrf_exempt
def query(request):
    post = request.POST
    point = Point(float(post['lng']),float(post['lat']))
    qs = WorldBorder.objects.filter(geom__contains=point)

    return HttpResponse(qs[0].geom.geojson) 
