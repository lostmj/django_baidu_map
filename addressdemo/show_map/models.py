# _*_ encoding:utf-8 _*_
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class address_info(models.Model):
# address_longitude为若干个坐标的经度
# address_latitude为若干个坐标的维度
# address_data为标记上所需要显示的数据
    longitude = models.FloatField()
    latitude = models.FloatField()
    data = models.CharField(max_length=200)
