from django.urls import path, re_path
from . import views

urlpatterns = [
    path('test_request/', views.test_request, name = 'test_request'),
]