from django.shortcuts import render

from django.http import JsonResponse
import json

# Create your views here.
def home(request):

    return render(request, 'index.html')

def senddata(request):
    postdata = json.loads(request.body.decode('utf-8'))
    
    name = postdata['name']
    datas = {
        'succes':True,
        'name':name
    }
    return JsonResponse(datas, safe=False)