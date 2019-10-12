from django.shortcuts import render

from django.http import JsonResponse
import json
from .models import *
# Create your views here.
def home(request):

    return render(request, 'index.html')

def senddata(request):
    # postdata = json.loads(request.body.decode('utf-8'))
    is_success = False
    img = request.FILES.get('file')
    name = request.POST.get('name')
    username = request.POST.get('username')
    phone = request.POST.get('phone')
    email = request.POST.get('email')
    try:
        myimg = MyImage(image = img, name = name, username = username, phone = phone, email = email)
        myimg.save()
        is_success = True
    except:
        is_success = False

    #name = postdata['file']
    datas = {
        'succes':True,
        'name':name,
        'username':username
    }
    return JsonResponse(datas, safe=False)