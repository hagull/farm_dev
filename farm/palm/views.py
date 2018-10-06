from django.shortcuts import render, get_object_or_404
from .models import Gcg, Anode, Snode, AnodeLog
import requests
from data.protocol_processing import *
from accounts.models import User

def base(request):
    return render(request, 'palm/base.html', {})
def index(request):
    user = request.user
    gcg = user.gcg_set.all()[0]
    snode = gcg.snode_set.all().filter(snode_type = 't')
    anode = gcg.anode_set.all()

    house = request.GET.get('house', '')
    type = request.GET.get('type', '')

    # 그래프를 만들기 위한 인자를 만드는 함수를 넣는다
    graph_data = None
    if house:
        if type:
            # house type 두개다 있는경우
            user = request.user
            gcg = get_object_or_404(Gcg, user = user, id = house)
            snode = Snode.objects.filter(gcg = gcg, snode_type = type)
            anode = Anode.objects.filter(gcg = gcg)
            # 그래프를 만들기 위한 인자를 만드는 함수를 넣는다
            graph_data = None
            pass
        else:
            # house 만 있을경우
            user = request.user
            gcg = get_object_or_404(Gcg, user = user, id = house)
            snode = Snode.objects.filter(gcg = gcg, snode_type = 't')
            anode = Anode.objects.filter(gcg = gcg)
            pass

    return render(request, 'index/index.html', {
        'user' : user,
        'gcg' : gcg,
        'snode' : snode,
        'anode' : anode,
    })

def control(request):
    user = request.user
    gcg = user.gcg_set.all()[0]
    snode = gcg.snode_set.all()
    anode = gcg.anode_set.all()
    gcg_cctv = gcg.gcgcctv_set.filter(cctv_type = 'i')
    cctv_exists = gcg.gcgcctv_set.filter(cctv_type = 'o').exists()
    type = request.GET.get('type', '')
    house = request.GET.get('house', '')
    all_house_cctv = None
    house_cctv = None
    if house == 'out_all':
        user = request.user
        gcg = user.gcg_set.all()
        all_house_cctv = user.allhousecctv_set.all()
        house_cctv = gcg[0].gcgcctv_set.filter(cctv_type = 'o')

        for gcg_query in gcg:
            before_house_cctv = gcg_query.gcgcctv_set.filter(cctv_type = 'o')
            house_cctv = house_cctv.union(before_house_cctv)
        # all_house_cctv 는 전체동( 한개농가 )의 외부 cctv의 부분
        # house_cctv는 각 동의 실외 cctv
    elif house == 'in_all':
        user = request.user
        gcg = user.gcg_set.all()
        house_cctv = gcg[0].gcgcctv_set.filter(cctv_type = 'i')
        for gcg_query in gcg:
            before_house_cctv = gcg_query.gcgcctv_set.filter(cctv_type = 'i')
            house_cctv = house_cctv.union(before_house_cctv)
    elif house:
        gcg = get_object_or_404(Gcg, id = house, user = user)
        snode = gcg.snode_set.all()
        anode = gcg.anode_set.all()
        if type:
            user = request.user
            gcg = get_object_or_404(Gcg, user=user, id=house)
            snode = gcg.snode_set.all()
            anode = gcg.anode_set.all()
            gcg_cctv = gcg.gcgcctv_set.filter(cctv_type = type)
        else:
            user = request.user
            gcg = get_object_or_404(Gcg, id=house, user=user)
            snode = gcg.snode_set.all()
            anode = gcg.anode_set.all()
            gcg_cctv = gcg.gcgcctv_set.filter(cctv_type = 'i')
    # 현재 gcg 통신은 위의 request.get과 같이 처리 혹은 템플릿 자체에서도 가능할듯 함
    return render(request, 'control/cctv_control.html', {
        'user' : user,
        'gcg' : gcg,
        'snode' : snode,
        'anode' : anode,
        'gcg_cctv' : gcg_cctv,
        'cctv_exists' : cctv_exists,
        'all_house_cctv' : all_house_cctv,
        'house_cctv' : house_cctv,
    })

def control_log(request):
    user = request.user
    gcg = user.gcg_set.all()
    anode = gcg[0].anode_set.all()
    combined_anode_log = anode[0].anodelog_set.all()
    type = request.GET.get('type', '')
    house = request.GET.get('house', '')
    # type / house 는 이후 조회기능을 구현할때 사용 control view함수와 비슷하게 구현하면 될듯함

    for gcg_query in gcg:
        anode = gcg_query.anode_set.all()
        for anode_query in anode:
            anode_log = anode_query.anodelog_set.all()
            combined_anode_log = combined_anode_log.union(anode_log)
    combined_anode_log.order_by('-created_at')
    return render(request, 'control/control_log.html', {
        'user' : user,
        'gcg' : gcg,
        'combined_anode_log' : combined_anode_log
    })


def category(request):
    pass
def record(request):
    pass
def past_record(request):
    pass

def gcg_page(request):
    user = request.user
    gcg = user.gcg_set.all()
    return render(request, 'settings/gcg_page.html', {
        'gcg' : gcg,
    })

def gcg_detail(request, gcg_serial):
    user = request.user
    gcg = get_object_or_404(Gcg, user = user, serial_num = gcg_serial)
    user_ip = user.profile.ip_address
    user_port = user.profile.ip_port
    ap3_1 = AP3_1_GCG(gcg_id = gcg_serial, version = 1, frame_type = 0, security = 0, sequence_number = 1)
    protocol = ap3_1.gcg_info(value1=1)
    url = 'http://{}:{}/{}'.format(user_ip, user_port, protocol)
    response = requests.get(url=url)
    protocol = response.text[9:-11]
    ap3_2 = AP3_2(protocol=protocol)
    gcg_id = None
    sw_ver = None
    node_num = None
    node_group = None
    node_info = []
    sensing_period_hour = None
    sensing_period_min = None
    sensing_period_sec = None
    gcg_state = None
    comm_error_num = None
    service_error_num = None
    etc = None
    split_protocol = {}
    if ap3_2.command_type == '01':
        ap3_2 = AP3_2_GCG(protocol=protocol)
        if ap3_2.payload == '01':
            split_protocol = ap3_2.gcg_info()
        elif ap3_2.payload == '02':
            split_protocol = ap3_2.gcg_response()
    else:
        pass
    split_protocol['url'] = url
    return render(request, 'settings/gcg_detail.html', split_protocol)
# Create your views here.
