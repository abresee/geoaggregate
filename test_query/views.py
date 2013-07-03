from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.gis.geos import Point
from django.template import RequestContext
from .models import WorldBorder

def index(request):
    'Just a Map, yo'
    return render_to_response('test_query/index.html',
        context_instance=RequestContext(request))

def query(request):
    post = request.POST
    point = Point(float(post['lng']),float(post['lat']))
    qs = WorldBorder.objects.filter(geom__contains=point)
    print(qs)

    return HttpResponse("".join([i.name for i in qs])) 
