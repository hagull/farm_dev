from django.db import models
from django.conf import settings
from django.urls import reverse

# Gcg 모델 정의 Gcg
# Gcg와 GcgInfo를 나눌필요는 없어보임 그이유는 자주 수정될 이유가 없는 테이블이고
# 수정된 부분도 인포의 일부분이기때문에 이부분을 로그로 남김 ex) sensing_periode/ Error
class Gcg(models.Model):
    STATE_TYPE = (
        ('n', 'Normal'),
        ('b', 'Battery_Error'),
        ('v', 'Voltage_Error'),
        ('c', 'Communication_Error'),
        ('u', 'Unknown Error'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    serial_num = models.IntegerField()
    node_num = models.IntegerField()
    node_group = models.IntegerField()
    # 이부분은 node_id가 들어갈 부분인데 gcg와 1:N관계로 있는 snode들의 그룹을 의미하므로 없어도 될 항복
    sensing_periode = models.DateTimeField()
    gcg_state = models.CharField(max_length=1, choices=STATE_TYPE)
    comm_error_num = models.IntegerField()
    service_error_num = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Gcg {} of {}'.format(self.serial_num, self.user.username)
class GcgLog(models.Model):
    # Gcg Info 중에서 로그로 남길부분들을 정하여서 적는것이 좋을듯
    # 이는 Gcg와의 통신로그와 구별시킬지, 합쳐도 무방할지
    # 합쳐도 무방하다고 생각 자주 수정될 테이블은 아니기때문에
    pass

# Snode 모델 정의
# Snode와 SnodeInfo를 구분할 필요는 마찬가지로 없다고 생각
class Snode(models.Model):
    STATE_TYPE = (
        ('n', 'Normal'),
        ('s', 'Sensor_Error'),
        ('b', 'Battery_Error'),
        ('v', 'Voltage_Error'),
        ('c', 'Communication_Error'),
        ('u', 'Unknown_Error'),
    )
    MONITOR_TYPE = (
        ('p', 'Passive'),
        ('e', 'Emergency'),
    )
    gcg = models.ForeignKey('Gcg', on_delete=models.PROTECT)
    serial_num = models.IntegerField()
    sw_ver = models.IntegerField()
    register_num = models.IntegerField()
    register_date = models.DateTimeField()
    node_state = models.CharField(max_length=1, choices=STATE_TYPE)
    monitor_mode = models.CharField(max_length=1, choices=MONITOR_TYPE)
    comm_error_num = models.IntegerField()
    service_error_num = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Snode {}, {}'.format(self.serial_num, self.gcg)

class SnodeValue(models.Model):
    SENSOR_TYPE = (
        ('t', 'Temperature'),
        ('h', 'Humidity'),
        ('th', 'Temperature_Humidity'),
        ('l', 'Light'),
        ('ws', 'Wind_Speed'),
        ('wd', 'Wind_Direction'),
        ('rf', 'Rain_Fall'),
        ('st', 'Soil_Temperature'),
        ('sh', 'Soil_Humidity'),
        ('ph', 'pH'),
        ('ec', 'EC'),
    )
    snode = models.ForeignKey('Snode', on_delete=models.PROTECT)
    snode_type = models.CharField(max_length=2, choices=SENSOR_TYPE)
    snode_value = models.CharField(max_length=100)

    created_at = models.DateTimeField(auto_now_add=True)
    # snode_value = models.IntegerField()
    # CharField 를 선택한 이유는 한개의 센서가 다수의 센싱값을 보내기때문
    def __str__(self):
        return 'Value {} of Snode {}'.format(self.snode_value, self.snode.serial_num)
class SnodeLog(models.Model):
    # 이도 마찬가지 Snode에 관한 로그기록
    # 이도 나중에 통합될수도
    pass
# Anode 모델 정의
# 마찬가지로 Anode 와 AnodeInfo를 구분할 필요는 없다고 생각
class Anode(models.Model):
    STATE_TYPE = (
        ('n', 'Normal'),
        ('s', 'Sensor_Error'),
        ('b', 'Battery_Error'),
        ('v', 'Voltage_Error'),
        ('c', 'Communication_Error'),
        ('u', 'Unknown_Error'),
    )
    OPERATING_TYPE = (
        ('p', 'Passive'),
        ('e', 'Emergency'),
    )
    gcg = models.ForeignKey('Gcg', on_delete=models.PROTECT)
    serial_num = models.IntegerField()
    sw_ver = models.IntegerField()
    register_num = models.IntegerField()
    register_date = models.DateTimeField()
    node_state = models.CharField(max_length=1, choices=STATE_TYPE)
    operating_mode = models.CharField(max_length=1, choices=OPERATING_TYPE)
    comm_error_num = models.IntegerField()
    service_error_num = models.IntegerField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return 'Anode {}, {}'.format(self.serial_num, self.gcg)
class AnodeValue(models.Model):
    ANODE_TYPE = (
        ('oc', 'Open_Close_Motor'),
        ('ef', 'Extractor_Fan'),
        ('wm', 'Watering_Motor'),
        ('ns', 'Nutrient_Supply'),
        ('lc', 'Light_Control'),
        ('cc', 'Co2_Control'),
        ('dh', 'Dehumidifier'),
        ('hf', 'Humidifier'),
        ('ve', 'Valve_Equipment'),
    )
    anode = models.ForeignKey('Anode', on_delete=models.PROTECT)
    anode_type = models.CharField(max_length=2, choices = ANODE_TYPE)
    anode_value = models.CharField(max_length=100)
    # anode_value = models.CharField()
    # 마찬가지의 이유
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return 'Value {} of Anode {}'.format(self.anode_value, self.anode.serial_num)
class AnodeLog(models.Model):
    # 이것역시 보류사항
    pass
# Vegetable Record 모델 정의
class Category(models.Model):
    VEGI_TYPE = (
        ('aaa', '오이'),
        ('aab', '딸기'),
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    category = models.CharField(max_length=3, choices=VEGI_TYPE, default=None)
    def __str__(self):
        return 'Category : {}'.format(self.get_category_dispaly())
class Record(models.Model):
    category = models.ForeignKey('Category', on_delete=models.PROTECT, default=None)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
# Demo 버전의 항목이 정해지면 그때 추가하여 진행
# Create your models here.
