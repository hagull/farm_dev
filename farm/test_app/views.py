from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context

def test_request(request):
    return render(request, 'test_app/test_request.html', {
        'user' : request.user,
        'test_gcg' : request.user.testgcg_set.all()[0],
    })
# Create your views here.
