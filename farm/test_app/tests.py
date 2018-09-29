from django.test import TestCase
from protocol_processing import *
import requests
'''def anode_request(request, gcg_id, anode_id):
    user = request.user
    gcg = get_object_or_404(Gcg, user = user, id = gcg_id)
    anode = get_object_or_404(Anode, gcg = gcg, id = anode_id)
    hex_anode = hex(anode_id)[2:].rjust(2, '0')
    hex_gcg = hex(gcg_id)[2:].rjust(2, '0')
    url = 'http://' + user.profile.ip_address + ':' + str(user.profile.ip_port)
    protocol = '0x'+hex_gcg+hex_anode
    params = {'protocol' : protocol}
    r = requests.get(url= url, params=params)'''
    # 이때 r 은 응답메세지로 응답메세지에 대한 처리도 해주어야한다
    # - > 일반적으로 응답메세지 정보들을 로그로 기록하는 역할을 하게될것
    # 위의 처리가 끝난 후에는 return 값으로 기존페이지로 리턴
    # return reverse(url / args = ) 와 같이
    # args = user / get params = > type / house 등의 정보들을 보낸다.
# Create your views here.
# Create your tests here.
def main():

    url1 = 'http://211.205.5.125:2000/0x01000000000100000001010101'
    url2 = 'http://211.205.5.125:2000/0x01000000000100000001010201000200'
    response = requests.get(url = url1)
    protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol = protocol)
    split_protocol = {}
    if ap3_2.command_type == '01':
        ap3_2 = AP3_2_GCG(protocol = protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.gcg_info()
        elif ap3_2.payload == '02':
            split_protocol = ap3_2.gcg_response()
    else:
        pass
    return print('gcg_id = {}'.format(split_protocol['gcg_id'])),\
            print('gcg_version = {}'.format(ap3_2.version)),\
            print('gcg_sequence = {}'.format(ap3_2.sequence)),\
            print(split_protocol),\
            print(protocol)
main()


