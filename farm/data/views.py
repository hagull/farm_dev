from django.shortcuts import render, get_object_or_404
from palm.models import Gcg, Anode
import requests
#import requests


def anode_request(request, gcg_id, anode_id):
    user = request.user
    gcg = get_object_or_404(Gcg, user = user, id = gcg_id)
    anode = get_object_or_404(Anode, gcg = gcg, id = anode_id)
    hex_anode = hex(anode_id)[2:].rjust(2, '0')
    hex_gcg = hex(gcg_id)[2:].rjust(2, '0')
    url = 'http://' + user.profile.ip_address + ':' + str(user.profile.ip_port)
    protocol = '0x'+hex_gcg+hex_anode
    params = {'protocol' : protocol}
    r = requests.get(url= url, params=params)
    # 이때 r 은 응답메세지로 응답메세지에 대한 처리도 해주어야한다
    # - > 일반적으로 응답메세지 정보들을 로그로 기록하는 역할을 하게될것
    # 위의 처리가 끝난 후에는 return 값으로 기존페이지로 리턴
    # return reverse(url / args = ) 와 같이
    # args = user / get params = > type / house 등의 정보들을 보낸다.
# Create your views here.
