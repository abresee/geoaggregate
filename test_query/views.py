# Create your views here.
from django.shortcuts import render_to_response
import simplejson

def index(request):
    'Map, yo'
    return render_to_response('test_query/index.html')
