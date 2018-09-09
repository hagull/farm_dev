from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader, Context

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
# Create your views here.
