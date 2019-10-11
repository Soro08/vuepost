from django.shortcuts import render

from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def home(request):

    return render(request, 'index.html')

def senddata(request):
    # postdata = json.loads(request.body.decode('utf-8'))

    img = request.FILES.get('file')
    name = request.POST.get('name')
    username = request.POST.get('username')
    myimg = MyImage(image = img)
    myimg.save()

    #name = postdata['file']
    datas = {
        'succes':True,
        'name':name,
        'username':username
    }
    return JsonResponse(datas, safe=False)