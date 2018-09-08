from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context

def test_request(request):
    user = request.user
    return render(request, 'test_app/test_request.html', {
        'user' : user,
        'test_gcg' : user.testgcg_set.all()[0],
    })
# Create your views here.
