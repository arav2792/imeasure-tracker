from django.db import models
import datetime
from datetime import date
from datetime import timedelta as tdelta
from django.utils import timezone
# Create your models here.
class Update(models.Model):
    inidate=timezone.now
    Date = models.DateField(null=False, blank=False, default=inidate)
    Topic = models.CharField(max_length=100,null=False)
    From_Engineer = models.CharField(max_length=100,null=False)
    Description = models.TextField(null=True, blank=False)
    Status = models.TextField(null=False, default='Active')
