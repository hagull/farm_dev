from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.template import RequestContext, loader, Context
from .protocol_processing import AP3_2
from hikvisionapi import Client
import cv2
import time
from django.views.decorators import gzip
def test_request(request):
    user = request.user
    test_gcg = None
    if user.testgcg_set.exists():
        test_gcg = user.testgcg_set.all()[0]
    return render(request, 'test_app/test_request.html', {
        'user' : user,
        'test_gcg' : test_gcg,
    })
def test_post(request):

    choice = request.POST.get('choice', '')

    return render(request, 'test_app/test_post.html', {
        'value' : choice,
        })
def test_get(request):
    value = request.GET.get('house', '')
    # if 문을 사용하여 request 발생시키면 될듯하다.
    return render(request, 'test_app/test_get.html', {
        'value' : value,
    })
def test_protocol(request):
    ap3 = AP3_2('0x0101010101010101010111010120102013123514532454235234234')
    return HttpResponse(ap3.version)
def test_dict(request):
    dict = {
        '1node_id' : {
            'id' : 1,
            'serial':2,
        },
        '2node_id' : {
            'id' : 2,
            'serial' : 3,
        },
    }
    return render(request, 'test_app/test_dict.html', dict)
# Create your views here.
def index1(request):
    return render(request, 'test_app/index.php')
def index2(request):
    return render(request, 'test_app/index.html')
def index3(request):
    return render(request, 'test_app/index.html')

