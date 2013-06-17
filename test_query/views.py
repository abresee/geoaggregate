import simplejson
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.contrib.gis.geos import Point
from django.views.decorators.csrf import csrf_exempt
from .models import WorldBorder

def index(request):
    'Just a Map, yo'
    return render_to_response('test_query/index.html')

@csrf_exempt
def query(request):
    post=request.POST
    point = Point(float(post['lng']),float(post['lat']))
    print(point)
    qs = WorldBorder.objects.filter(geom__contains=point)
    print(qs)
    
    return HttpResponse("".join([i.name for i in qs])) 
