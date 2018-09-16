from django.urls import path, re_path
from . import views
app_name = 'data'
urlpatterns = [
    path('anode_request/<int:gcg_id>/<int:anode_id>', views.anode_request, name = 'anode_request'),
]