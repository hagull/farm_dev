from django.urls import path, re_path
from . import views
app_name = 'palm'
urlpatterns = [
    path('', views.base, name='base'),
    path('index/', views.index, name = 'index'),

    path('control/', views.control, name = 'control'),
    path('control/log/', views.control_log, name = 'control_log'),

    path('category/', views.category, name = 'category'),
    path('category/<str:category>/record', views.record, name = 'record'),
    path('category/past_record', views.past_record, name = 'past_record'),
    # 아마도 설정페이지가 될 부분
    path('gcg_page/', views.gcg_page, name = 'gcg_info'),
    path('gcg_page/gcg_detail/<str:gcg_serial>', views.gcg_detail, name = 'gcg_detail'),
    # Vegetable_Record 은 시장조사( 시범농장 ) 직전 혹은 진행하면서 개발해도 좋을듯 함
    # etc 설정페이지 데이터페이지 고객센터 등 페이지 추가예정
]
