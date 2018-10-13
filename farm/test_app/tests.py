from django.test import TestCase
from protocol_processing import *
import requests


import cv2
import numpy as np


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
def main1():

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
    node_id = []
    for a in split_protocol['node_info']:
        node_id.append(a[:10])
    return print('gcg_id = {}'.format(split_protocol['gcg_id'])),\
            print('gcg_version = {}'.format(ap3_2.version)),\
            print('gcg_sequence = {}'.format(ap3_2.sequence)),\
            print(split_protocol),\
            print(protocol),\
            print('node_info = {}'.format(split_protocol['node_info'])),\
            print('node_id = {}'.format(node_id))
def main2():
    url1 = 'http://211.205.5.125:2000/0x01000000000100000001010102'
    response = requests.get(url=url1)
    return print(response.text)
# payload 01 test
def main3():
    snode_id = ['4200000001', '4200000002', '4200000003', '4200000004', '4200000005', '4200000006', '4200000007',
               '4200000008']
    anode_id = ['8000000001']
    IP = 'http://211.205.5.125:2000/'
    ver = '01'
    frametype = '00'
    security = '00'
    sequence = '0000'
    gcg_id = '0100000001'
    cmd_type = '02'
    payload_type = '01'
    # 01/03/04
    value1 = '07'
    # value1 01 ~ 09
    # 02 03 사이에서 뭔가 이상한데
    # 오류 - 프로토콜의 value1 값은 변하고 변한 프로토콜을 전송하는데 이전에 전송했던 값이 출력됨
    value2 = '06'
    value3 = ''
    value3 = value3.join(snode_id)
    cmd2_pay1_url = IP + '0x' + ver + frametype + security + sequence + gcg_id + cmd_type + payload_type + value1 + value2 + value3
    response = requests.get(url = cmd2_pay1_url)
    protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol = protocol)
    split_protocol = {}
    if ap3_2.command_type == '02':
        ap3_2 = AP3_2_NODE(protocol = protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.snode_info()
        else:
            pass
    return print(cmd2_pay1_url), \
            print(protocol), \
            print(split_protocol),\
            print(ap3_2.payload)
# payload 03 Test
def main4():
    anode_id = ['8000000001']
    IP = 'http://211.205.5.125:2000/'
    ver = '01'
    frametype = '00'
    security = '00'
    sequence = '0000'
    gcg_id = '0100000001'
    cmd_type = '02'
    payload_type = '03'
    # 01/03/04
    value1 = '01'
    value2 = '01'
    value3 = ''
    value3 = value3.join(anode_id)
    cmd2_pay1_url = IP + '0x' + ver + frametype + security + sequence + gcg_id + cmd_type + payload_type + value1 + value2 + value3
    response = requests.get(url=cmd2_pay1_url)
    protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol=protocol)
    split_protocol = {}
    if ap3_2.command_type == '02':
        ap3_2 = AP3_2_NODE(protocol=protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.snode_info()
        elif ap3_2.payload == '03':
            split_protocol = ap3_2.anode_info()
    return print(cmd2_pay1_url), \
           print(protocol), \
           print(split_protocol), \
           print(ap3_2.payload)
# payload type 0x04 Test
def main5():
    anode_id = ['8000000001']
    IP = 'http://211.205.5.125:2000/'
    ver = '01'
    frametype = '00'
    security = '00'
    sequence = '0000'
    gcg_id = '0100000001'
    cmd_type = '02'
    payload_type = '04'
    # 01/03/04
    value1 = anode_id[0]
    # value1 01 ~ 09
    # 02 03 사이에서 뭔가 이상한데
    # 오류 - 프로토콜의 value1 값은 변하고 변한 프로토콜을 전송하는데 이전에 전송했던 값이 출력됨
    value2 = '00'
    value3 = '01'
    value4 = '00'
    cmd2_pay1_url = IP + '0x' + ver + frametype + security + sequence + gcg_id + cmd_type + payload_type + value1 + value2 + value3 + value4
    response = requests.get(url=cmd2_pay1_url)
    protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol=protocol)
    split_protocol = {}
    if ap3_2.command_type == '02':
        ap3_2 = AP3_2_NODE(protocol=protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.snode_info()
        elif ap3_2.payload == '03':
            split_protocol = ap3_2.anode_info()
        elif ap3_2.payload == '04':
            split_protocol = ap3_2.anode_response()
        else:
            pass
    return print(cmd2_pay1_url), \
           print(protocol), \
           print(split_protocol), \
           print(ap3_2.payload)
# ap3_1과 같이 진행 payload 01 03 04
def main6():
    snode_id = ['4200000001', '4200000002', '4200000003', '4200000004', '4200000005', '4200000006', '4200000007',
                '4200000008']
    IP = 'http://211.205.5.125:2000/'
    ver = '01'
    frametype = '00'
    security = '00'
    sequence = '0000'
    gcg_id = '0100000001'
    cmd_type = '02'
    payload_type = '01'
    # 01/03/04
    value1 = 1
    # value1 01 ~ 09
    # 02 03 사이에서 뭔가 이상한데
    # 오류 - 프로토콜의 value1 값은 변하고 변한 프로토콜을 전송하는데 이전에 전송했던 값이 출력됨
    value2 = 8
    value3 = ''
    value3 = value3.join(snode_id)
    ap3_1 = AP3_1_NODE(gcg_id = gcg_id)
    request_protocol = ap3_1.snode_info(payload_type = 1, value1 = value1, value2 = value2, value3 = value3)
    cmd2_pay1_url = IP + request_protocol
    response = requests.get(url=cmd2_pay1_url)
    response_protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol=response_protocol)
    split_protocol = {}
    if ap3_2.command_type == '02':
        ap3_2 = AP3_2_NODE(protocol=response_protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.snode_info()
        elif ap3_2.payload == '03':
            split_protocol = ap3_2.anode_info()
        elif ap3_2.payload == '04':
            split_protocol = ap3_2.anode_response()
        else:
            pass
    return print(request_protocol),\
            print(cmd2_pay1_url), \
            print(response_protocol), \
            print(split_protocol), \
            print(ap3_2.payload)

main3()
# 현재 gcg 1에 연결되어 있는 node의 serial num


cap = cv2.VideoCapture("rtsp://admin:Farmpalm!@211.205.5.125:554/Streaming/Channels/101")
# cap = cv2.VideoCapture("rstp://admin:Falmpalm!@211.205.5.125:554/doc/page/previw.asp")
# cap.open("rtsp://admin:Farmpalm!@211.205.5.125:554/Streaming/Channels/1")
i = 0
while(True):
    ret, frame = cap.read()

    # Our operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Display the resulting frame
    cv2.imshow('frame', ret)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    i += 1
    print(i)
cap.release()
cv2.destroyAllWindows()



# 현재 gcg 1에 연결되어 있는 node의 serial num


