from django.db import models
import datetime
from django.utils.translation import gettext as _
from datetime import date
from datetime import timedelta as tdelta
from django.utils import timezone
import calendar


# Create your models here.
class Post(models.Model):
    today = datetime.date.today()
    years = today.year
    Year = models.PositiveSmallIntegerField(blank=False, null=False, db_column='yeer',default=years)

    weeknumbers = date.today().isocalendar()[1]
    weeknumber = "Week {}".format(weeknumbers)
    Week = models.CharField(max_length=20, blank=False, null=True, db_column='weekno',default=weeknumber)

    today = datetime.date.today()
    x=calendar.month_name[today.month]
    Month = models.CharField(max_length=100, null=False, blank=False, db_column='menth',default=x)
    #Date = models.DateField(_("Date"), default=datetime.date.today, null=False, blank=False, db_column='dete')

    #inidate=timezone.now().date()
    inidate=datetime.date.today().strftime('%Y-%m-%d')
    Date = models.DateField(null=False, blank=False, db_column='dete',default=inidate)


    curtime = datetime.datetime.now()
    currenttime = curtime.hour
    if currenttime in (8,9,10,11,12,13,14,15):
        y = "APAC"
    elif currenttime in (16,17,18,19,20,21,22):
        y = "EMEA"
    else:
        y = "USA"
    Shift = models.TextField(null=False, db_column='shyft', default=y)

    weekno = datetime.datetime.today().weekday()
    if weekno < 5:
        x = ("Weekday")
    else:
        x = ("Weekend")
    Day_Of_Week = models.TextField(null=False, db_column='dayofweek', default=x)
    Start_Time = models.CharField(max_length=8,blank=False,null=True,db_column='stime')
    Responded_Time =  models.CharField(max_length=8,blank=False,null=True,db_column='rtime')
    Time_spent = models.CharField(max_length=8,blank=False,null=True, db_column='wtime')
    Responsible_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='respteam')
    False_Alarm = models.TextField(null=False, db_column='falsealarm',default="No")
    Incident_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='itype')
    Priority = models.CharField(max_length=10 ,null=False, db_column='priority', default='None')
    General_Health_Check = models.CharField(max_length=100, null=True, blank=True, default='NA', db_column='ghcname')
    Alert = models.CharField(max_length=100, null=True, blank=True, default='NA', db_column='alertname')
    Task = models.CharField(max_length=100, null=True, blank=True, default='NA', db_column='taskname')
    If_Others_Please_Specify = models.CharField(max_length=100, null=False, blank=True, db_column='others', default='NA')
    Description = models.TextField(null=True, blank=False, db_column='descrp')
    Environment = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='env')
    Host_Type = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='hostype')
    Host_Name = models.CharField(max_length=100, null=True, blank=False, db_column='hostname')
    Source_of_Alert = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='source')
    Mode_of_Alert = models.TextField(null=False, db_column='mode', default="Manual")
    NOC_Engineer = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='engineer')
    Remediation = models.TextField(null=True, blank=True, default='NA', db_column='remediation',)
    Escalated = models.CharField(max_length=100, null=False, blank=False, default='No', db_column='escalated')
    Escalated_Reason = models.CharField(max_length=100, null=True, blank=True, default='NA', db_column='escreason')
    Status = models.CharField(max_length=100, null=True, blank=True, default='Resolved', db_column='status')
    Escalated_to = models.CharField(max_length=100, null=True, blank=True, default='NA', db_column='escalatedto')
    Resolved_by_Team = models.CharField(max_length=100, null=True, blank=False, default='Please select', db_column='resolvedteam')
    Resolved_by_Engineer = models.CharField(max_length=30, null=False, default='noc', db_column='resolvedby')
    Resolution = models.TextField(null=True, blank=False, db_column='resolution')
    Comments = models.TextField(null=True, blank=False, db_column='comments')
    #Interval = models.IntegerField(blank=True, null=False, db_column='intrval')
    #Complexity = models.TextField(blank=True, null=False, db_column='cmplx')

class Schedules(models.Model):
    title = models.CharField(max_length = 200, null=True)
    image = models.ImageField(upload_to='media/')
