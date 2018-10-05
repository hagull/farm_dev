from django.urls import path, re_path
from . import views

urlpatterns = [
    path('test_request/', views.test_request, name = 'test_request'),
    path('test_post/', views.test_post, name = 'test_post'),
    path('test_get/', views.test_get, name = 'test_get'),
    path('test_protocol/', views.test_protocol, name = 'test_protocol'),
    path('test_dict', views.test_dict, name = 'test_dict'),
]