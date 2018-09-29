import struct
# shell 환경에서는 제대로 출력이 안되므로 이 스크립트 안에서 해결하도록 하자

# AP3-1 server => Gcg 통신 프로토콜 클래스 정의
class AP3_1:
    def __init__(self, command_type, gcg_id = '0', version = 1, frame_type = 0, security = 0, sequence_number = 0):
        self.frame_header = '0x'
        self.version = hex(version)[2:].rjust(2, '0')
        self.frame_type = hex(frame_type)[2:].rjust(2, '0')
        self.security = hex(security)[2:].rjust(2, '0')
        self.sequence = hex(sequence_number)[2:].rjust(4, '0')
        # self.gcg_id = hex(gcg_id)[2:].rjust(10, '0')
        self.gcg_id = gcg_id.rjust(10, '0')
        self.command_type = hex(command_type)[2:].rjust(2, '0')
        self.frame_header = self.frame_header + self.version + self.frame_type + self.security + self.sequence + self.gcg_id + self.command_type
# command type = 0x01
class AP3_1_GCG(AP3_1):
    def __init__(self, command_type = 1, gcg_id = 0, version=1, frame_type=0, security=0, sequence_number=0):
        super().__init__(command_type, gcg_id, version, frame_type, security, sequence_number)
    # payload type 0x01이면 호출 - 온실통합제어기 정보 데이터 전송
    def gcg_info(self, payload_type = 1, value1 = 0):
        payload_type = hex(payload_type)[2:].rjust(2, '0')
        value1 = hex(value1)[2:].rjust(2, '0')
        protocol = self.frame_header + payload_type + value1
        return protocol
    # payload type 0x02이면 호출 - 온실통합제어기 정보수집주기 설정요청
    def gcg_request(self, payload_type = 2, value1 = 1, value2_hour = 0, value2_min = 0, value2_sec = 0):
        payload_type = hex(payload_type)[2:].rjust(2, '0')
        value1 = hex(value1)[2:].rjust(2, '0')
        value2_hour = hex(value2_hour)[2:].rjust(2, '0')
        value2_min = hex(value2_min)[2:].rjust(2, '0')
        value2_sec = hex(value2_sec)[2:].rjust(2, '0')
        value2 = value2_hour + value2_min + value2_sec
        protocol = self.frame_header + payload_type + value1 + value2
        return protocol
# command type = 0x02
class AP3_1_NODE(AP3_1):
    def __init__(self, command_type = 2, gcg_id = 0, version=1, frame_type=0, security=0, sequence_number=0):
        super().__init__(command_type, gcg_id, version, frame_type, security, sequence_number)
    # payload type 0x01 이면 호출 - 센서노드의 정보 데이터 전송
    def snode_info(self):
        pass
    # 0x02 - 센서노드 설정요청에 대한 응답
    def snode_request(self):
        pass
    # 0x03 - 제어노드 정보데이터 전송
    def anode_info(self):
        pass
    # 0x04 - 제어노드 설정요청에 대한 응답
    def anode_request(self):
        pass
# command type = 0x03
class AP3_1_CONTROL_GROUP(AP3_1):
    def __init__(self, command_type = 3, gcg_id = 0, version=1, frame_type=0, security=0, sequence_number=0):
        super().__init__(command_type, gcg_id, version, frame_type, security, sequence_number)
    # 0x01
    def group_info(self):
        pass
    # 0x02
    def group_request(self):
        pass
# command type = 0x04
class AP3_1_READ_LOG(AP3_1):
    def __init__(self, command_type = 4, gcg_id = 0, version=1, frame_type=0, security=0, sequence_number=0):
        super().__init__(command_type, gcg_id, version, frame_type, security, sequence_number)
    # 0x01
    def log_all(self):
        pass
    # 0x02
    def log_part(self):
        pass

# AP3-1 - END




# AP3-2 Gcg => server 통신 프로토콜 클래스 정의
class AP3_2:
    def __init__(self, protocol):
        self.protocol = protocol[2:]
        self.version = self.protocol[:2]
        self.frame_type = self.protocol[2:4]
        self.security = self.protocol[4:6]
        self.sequence = self.protocol[6:10]
        self.gcg = self.protocol[10:20]
        self.command_type = self.protocol[20:22]
        self.payload = self.protocol[22:24]
        self.value1 = self.protocol[24:26]
        self.value2 = self.protocol[26:]
# command type = 0x01
class AP3_2_GCG(AP3_2):
    def __init__(self, protocol):
        super().__init__(protocol)
    # payload type 0x01이면 호출 - 온실통합제어기 정보 데이터 전송
    def gcg_info(self):
        # gcg_info 클래스 호출시에 protocol의 value1 = 0x01이면 아래와같은 값들이 리턴되게 된다.
        if self.value1 == '01':
            # 3870개의 문자열 처리
            gcg_id = self.value2[:10]
            sw_ver = self.value2[10:12]
            node_num = self.value2[12:14]
            node_num_dec = int(node_num, 16)
            node_group_end = (120*32) + 14
            # node_num의 max = 32 min = 0
            node_group = self.value2[14:node_group_end]
            self.value2 = self.value2[node_group_end:]
            # node_group 는 node_num * 60byte의 크기를 가진다.
            # sever에서 node_group만 받아도 node_num 까지 처리가 가능
            # node_num = len(node_id)
            node_info = []
            split_protocol = {}
            # node_id 가 아니라 node_info이다. 이를 처리해주는것이 다시한번 필요
            for i in range(0, node_group_end-14, 120):
                node_info.append(node_group[i:i+120])
                # 이 반복문에 의해 60byte의 크기 120개의 문자열을 가진 데이터들이 리스트에 저장이된다.
            sensing_period_hour = self.value2[:2]
            sensing_period_min = self.value2[2:4]
            sensing_period_sec = self.value2[4:6]
            gcg_state = self.value2[6:8]
            comm_error_num = self.value2[8:12]
            service_error_num = self.value2[12:16]
            etc = self.value2[16:]
            split_protocol = {'gcg_id' : gcg_id,
                              'sw_ver' : sw_ver,
                              'node_num' : node_num,
                              'node_group' : node_group,
                              'node_info' : node_info,
                              'sensing_period_hour' : sensing_period_hour,
                              'sensing_period_min' : sensing_period_min,
                              'sensing_period_sec' : sensing_period_sec,
                              'gcg_state' : gcg_state,
                              'comm_error_num' : comm_error_num,
                              'service_error_num' : service_error_num,
                              'etc' : etc}
            # 리턴하기 전에 gcg_id나 sw_ver는 모두 16진수의 형태이므로 이를 10진수 형태로 바꿔줄 작업이 필요하다.
            return split_protocol
        # value1 = 0x02
        elif self.value1 == '02':
            # 10개의 문자열 처리
            gcg_id = self.value2
            split_protocol = {'gcg_id': gcg_id}
            return split_protocol
        # value1 = 0x03
        elif self.value1 == '03':
            # 2개의 문자열 처리
            sw_ver = self.value2
            split_protocol = {'sw_ver': sw_ver}
            return split_protocol
        # value1 = 0x04
        elif self.value1 == '04':
            # 3842개의 문자열 처리
            node_num = self.value2[:2]
            node_num_dec = int(node_num, 16)
            node_group_end = (node_num_dec * 120) + 2
            node_group = self.value2[2:node_group_end]
            node_info = []
            for i in range(0, node_group_end - 14, 120):
                node_info.append(node_group[i:i+120])
            split_protocol = {'node_num': node_num,
                              'node_group': node_group,
                              'node_info': node_info
                              }
            return split_protocol
        # value1 = 0x05
        elif self.value1 == '05':
            # 6개의 문자열 처리
            sensing_period_hour = self.value2[:2]
            sensing_period_min = self.value2[2:4]
            sensing_period_sec = self.value2[4:6]
            # 이를 데이터타임 객체로 변환하여 리턴하는것이 좋을듯
            split_protocol = {'sensing_period_hour': sensing_period_hour,
                              'sensing_period_min': sensing_period_min,
                              'sensing_period_sec': sensing_period_sec}
            return split_protocol
        # value1 = 0x06
        elif self.value1 == '06':
            # 2개의 문자열 처리
            gcg_state = self.value2
            split_protocol = {'gcg_state': gcg_state}
            return split_protocol
        # value1 = 0x07
        elif self.value1 == '07':
            # 4개의 문자열 처리
            comm_error_num = self.value2
            split_protocol = {'comm_error_num': comm_error_num}
            return split_protocol
        # value1 = 0x08
        elif self.value1 == '08':
            # 4개의 문자열 처리
            service_error_num = self.value2
            split_protocol = {'service_error_num': service_error_num}
            return split_protocol
        else:
            pass
    # payload type 0x02이면 호출 - 온실통합제어기 설정요청에 대한 응답
    def gcg_response(self):
        period_edit = None
        period_edit_state = None
        if self.value2 == '01':
            period_edit = True
            period_edit_state = 'Success'
        elif self.value2 == '02':
            period_edit = False
            period_edit_state = 'Error'
        else:
            pass
        split_protocol = {'period_edit' : period_edit,
                          'period_edit_state' : period_edit_state}
        return split_protocol
# command type = 0x02
class AP3_2_NODE(AP3_2):
    def __init__(self, protocol):
        super().__init__(protocol)
    # payload type 0x01 이면 호출 - 센서노드의 정보 데이터 전송
    def snode_info(self):
        pass
    # 0x02 - 센서노드 설정요청에 대한 응답
    def snode_response(self):
        pass
    # 0x03 - 제어노드 정보데이터 전송
    def anode_info(self):
        pass
    # 0x04 - 제어노드 설정요청에 대한 응답
    def anode_response(self):
        pass
# command type = 0x03
class AP3_2_CONTROL_GROUP(AP3_2):
    def __init__(self, protocol):
        super().__init__(protocol)
    # 0x01
    def group_info(self):
        pass
    # 0x02
    def group_response(self):
        pass
# command type = 0x04
class AP3_2_READ_LOG(AP3_2):
    def __init__(self, protocol):
        super().__init__(protocol)
    # 0x01
    def log_all(self):
        pass
    # 0x02
    def log_part(self):
        pass
# AP3-2 - END


