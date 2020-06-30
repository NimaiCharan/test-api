from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from .models import Test
from .serializers import TestSerializer

# Create your views here.

def index(request):
    if request.method =='GET':
        data =  Test.objects.all()
        
        #json_data = serializers.serialize('json', data)
        serializer = TestSerializer(data, many=True)

        return JsonResponse(serializer.data, safe=False)
    
    
    #return HttpResponse(json_data, content_type='application/json')
    #return render(request, 'index.html',{'data':json_data})
    
