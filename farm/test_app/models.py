from django.db import models
from django.conf import settings

class TestGcg(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    serial_num = models.IntegerField()
# Create your models here.
class Test(models.Model):
    pass