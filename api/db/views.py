from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
from .models import Dummy

# Create your views here.

def index(request):
    data =  Dummy.objects.all()
    
    json_data = serializers.serialize('json', data)
    
    return HttpResponse(json_data, content_type='application/json')
    #return render(request, 'index.html',{'data':json_data})
