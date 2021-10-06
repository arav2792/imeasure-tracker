from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from . import models
from django.utils.safestring import mark_safe
from django.forms import widgets
from django.db.models.fields import BLANK_CHOICE_DASH
from datetime import date
from bootstrap_datepicker_plus import DatePickerInput
from django.forms import ModelForm, widgets, DateTimeField, DateField, DateInput

class CreateArticle(forms.ModelForm):
    Year = forms.IntegerField(widget=forms.NumberInput(attrs={'title':'Enter the current Year','style': 'width: 55% !important; resize: vertical !important;'}))

    weeknumber = date.today().isocalendar()[1]
    Week = forms.CharField(initial=weeknumber, widget=forms.TextInput(attrs={'title':'Week number','style': 'width: 55% !important; resize: vertical !important;'}))

    Date = forms.CharField( widget=forms.TextInput(attrs={'title':'Current Date','style': 'width: 55% !important; resize: vertical !important;'}))

    shift_choices=(('APAC','APAC'),('EMEA','EMEA'),('USA','USA'))

    Shift = forms.ChoiceField(choices=shift_choices, widget=forms.RadioSelect(attrs={'id':'shiftid','title':'The shift in which alert was handled','style': 'width: 75% !important; resize: vertical !important;'}))

    weekchoice=(('Weekday','Weekday'),('Weekend','Weekend'))
    Day_Of_Week = forms.ChoiceField(choices=weekchoice, widget=forms.RadioSelect(attrs={'id':'weekid'}))

    Start_Time = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'HH:MM','title':'Mention the start time in 24 hour time format','style': 'width: 55% !important; resize: vertical !important;'}))

    #placeholder="HH:MM" size="13" title="Enter the time you spent" pattern=".+:.+"/
    Responded_Time = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'HH:MM','title':'Mention the Responded time in 24 hour time format','style': 'width: 55% !important; resize: vertical !important;'}))

    Time_spent = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'HH:MM','title':'Mention the Total time spent in 24 hour time format','style': 'width: 55% !important; resize: vertical !important;'}))
    MONTH_CHOICES = (
    ('January', 'January'),
    ('February', 'February'),
    ('March', 'March'),
    ('April', 'April'),
    ('May', 'May'),
    ('June', 'June'),
    ('July', 'July'),
    ('August', 'August'),
    ('September', 'September'),
    ('October', 'October'),
    ('November', 'November'),
    ('December', 'December'),
)
    #today = datetime.date.today()
    #months = ['January','February','March','April','May','June','July','August','September','October','November','December']
    #current_month = months[today.month]
    #months = today.month
    Month_empty = tuple(BLANK_CHOICE_DASH + list(MONTH_CHOICES))
    Month = forms.ChoiceField(choices=(Month_empty), widget=forms.Select(attrs={'title':'Enter the current Month','style': 'width: 55% !important; resize: vertical !important;'}))

    Res_team = (
    ('B2B - Core', 'B2B - Core'),
    ('B2B - Data', 'B2B - Data'),
    ('B2B - Reporting', 'B2B - Reporting'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data Infra', 'Data Infra'),
    ('Data Prod', 'Data Prod'),
    ('Data Science', 'Data Science'),
    ('Dev', 'Dev'),
    ('Dynamic Cretive', 'Dynamic Cretive'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('Growth IO', 'Growth IO'),
    ('Internal Tools', 'Internal Tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('omnom', 'omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webapp', 'Webapp'),
)
    Res_team_empty =  tuple(BLANK_CHOICE_DASH + list(Res_team))
    Responsible_Team = forms.ChoiceField(choices=(Res_team_empty), widget=forms.Select(attrs={'title':'Enter the Responsible Team','style': 'width: 55% !important; resize: vertical !important;'}))

    fse_alarm=(('Yes','Yes'),('No','No'))
    False_Alarm = forms.ChoiceField(choices=fse_alarm, widget=forms.RadioSelect(attrs={'id':'falseid','title':'Was the alert genuine?'}))

    inc_type = (
    ('Alert', 'Alert'),
    ('GHC', 'GHC'),
    ('Other', 'Other'),
    ('Task', 'Task'),
)
    inc_type_empty = tuple(BLANK_CHOICE_DASH + list(inc_type))
    Incident_Type = forms.ChoiceField(choices=(inc_type_empty), widget=forms.Select(attrs={'title':'Enter the type of incident','style': 'width: 55% !important; resize: vertical !important;'}))

    prior=(('P0','P0'),('P1','P1'),('P2','P2'),('None','None'))
    Priority = forms.ChoiceField(choices=prior, widget=forms.RadioSelect(attrs={'id':'priorityid','title':'The priority of alert as per policy'}))

    GHC = (
      ('Celery Dashboard check', 'Celery Dashboard check'),
      ('Dashboard monitoring', 'Dashboard monitoring'),
      ('Pipeline monitoring', 'Pipeline monitoring'),
      ('Storm Monitoring', 'Storm Monitoring'),
      ('NA', 'NA'),
    )
    ghc_empty = tuple(BLANK_CHOICE_DASH + list(GHC))
    General_Health_Check = forms.ChoiceField(choices=(ghc_empty), required=False, widget=forms.Select(attrs={'title':'Name of the GHC','style': 'width: 55% !important; resize: vertical !important;'}))

    Alert = (
       ('AWS Notifications', 'AWS Notifications'),
       ('Celery Infra Alerts', 'Celery Infra Alerts'),
       ('Celery Task Failure', 'Celery Task Failure'),
       ('CPU Utilization', 'CPU Utilization'),
       ('Disk Usage', 'Disk Usage'),
       ('Dotcom Alerts', 'Dotcom Alerts'),
       ('ECR Capacity', 'ECR Capacity'),
       ('EMR Job Failure', 'EMR Job Failure'),
       ('Hbase Alert', 'Hbase Alert'),
       ('Jenkins Job Failure', 'Jenkins Job Failure'),
       ('Outage', 'Outage'),
       ('Segment Error', 'Segment Error'),
       ('Storm Alert', 'Storm Alert'),
       ('Threatstack Alert', 'Threatstack Alert'),
       ('Thrift Alert', 'Thrift Alert'),
       ('NA', 'NA'),
       )
    alert_empty = tuple(BLANK_CHOICE_DASH + list(Alert))
    Alert = forms.ChoiceField(choices=(alert_empty), required=False, widget=forms.Select(attrs={'title':'Name of the Alert','style': 'width: 55% !important; resize: vertical !important;'}))

    Task = (
    ('Backup Audit', 'Backup Audit'),
    ('Deployment', 'Deployment'),
    ('EMR Job Check', 'EMR Job Check'),
    ('High Intent Segment Creation', 'High Intent Segment Creation'),
    ('Jenkins Job Failure', 'Jenkins Job Failure'),
    ('Long Running EMR Check', 'Long Running EMR Check'),
    ('Post-Deploy Health Check', 'Post-Deploy Health Check'),
    ('Quentin Job Failures validation', 'Quentin Job Failures validation'),
    ('Sentry Notification', 'Sentry Notification'),
    ('Spend Monitoring', 'Spend Monitoring'),
    ('NA', 'NA'),
    )
    task_empty = tuple(BLANK_CHOICE_DASH + list(Task))
    Task = forms.ChoiceField(choices=(task_empty), required=False, widget=forms.Select(attrs={'title':'Name of the task','style': 'width: 55% !important; resize: vertical !important;'}))


    If_Others_Please_Specify = forms.CharField(widget=forms.TextInput(attrs={'title':'If you entered the incident type as others, Please shed some light.','style': 'width: 55% !important; resize: vertical !important;'}))

    envi = (
    ('Production', 'Production'),
    ('Staging', 'Staging'),
    ('Test', 'Test'),
    ('Dev', 'Dev'),
    ('Local', 'Local'),
    ('Multiple', 'Multiple'),
    ('NA', 'NA'),
)
    envi_empty = tuple(BLANK_CHOICE_DASH + list(envi))
    Environment = forms.ChoiceField(choices=(envi_empty), widget=forms.Select(attrs={'title':'Enter the incident Environment','style': 'width: 55% !important; resize: vertical !important;'}))

    hosttype = (
    ('AWS Batch', 'AWS Batch'),
    ('AWS ECS', 'AWS ECS'),
    ('AWS EC2', 'AWS EC2'),
    ('AWS Elasticache', 'AWS Elasticache'),
    ('AWS EMR', 'AWS EMR'),
    ('AWS RDS', 'AWS RDS'),
    ('Batchie Patchie', 'Batchie Patchie'),
    ('Celery Worker', 'Celery Worker'),
    ('Docker Registry', 'Docker Registry'),
    ('Docker Server', 'Docker Server'),
    ('Hbase cluster', 'Hbase cluster'),
    ('Jenkins', 'Jenkins'),
    ('Load Balancer', 'Load Balancer'),
    ('Localhost', 'Localhost'),
    ('Luigi', 'Luigi'),
    ('NA', 'NA'),
    ('Other', 'Other'),
    ('Presto', 'Presto'),
    ('Puppet', 'Puppet'),
    ('puppet', 'Puppet'),
    ('Quentin', 'Quentin'),
    ('Storm Cluster', 'Storm Cluster'),
    ('Thrift Cluster', 'Thrift Cluster'),
)
    hosttype_empty = tuple(BLANK_CHOICE_DASH + list(hosttype))
    Host_Type = forms.ChoiceField(choices=(hosttype_empty), widget=forms.Select(attrs={'title':'Enter the host type','style': 'width: 55% !important; resize: vertical !important;'}))

    source = (
    ('AWS', 'AWS'),
    ('Celery', 'Celery'),
    ('Datadog', 'Datadog'),
    ('Icinga', 'Icinga'),
    ('Jenkins', 'Jenkins'),
    ('Logentries', 'Logentries'),
    ('NA', 'NA'),
    ('New Relic', 'New Relic'),
    ('Pingdom', 'Pingdom'),
    ('Sentry', 'Sentry'),
    ('Slack', 'Slack'),
    ('Threatstack', 'Threatstack'),
)
    source_empty = tuple(BLANK_CHOICE_DASH + list(source))
    Source_of_Alert = forms.ChoiceField(choices=(source_empty), widget=forms.Select(attrs={'title':'Enter the source of alert','style': 'width: 55% !important; resize: vertical !important;'}))

    mode=[('Email','Email'),('Manual','Manual'),('Slack','Slack')]
    Mode_of_Alert = forms.ChoiceField(choices=mode, widget=forms.RadioSelect(attrs={'id':'modeid','title':'Enter the mode of alert'}), initial="Manual")

    engineer= (
    ('Aravind Suresh', 'Aravind Suresh'),
    ('Gokul Harikrishnan', 'Gokul Harikrishnan'),
    ('Hajamoideen Jailaudeen','Hajamoideen Jailaudeen'),
    ('Jagan Babu', 'Jagan Babu'),
    ('Joel jaqfine', 'Joel jaqfine'),
    ('Kiren Aananth', 'Kiren Aananth'),
    ('Manikandan Sivaraj', 'Manikandan Sivaraj'),
    ('MIS team', 'MIS team'),
    ('Nirmal Kumar', 'Nirmal Kumar'),
    ('QA team', 'QA team'),
    ('Ramesh Krishna', 'Ramesh Krishna'),
    ('Sathish Basker', 'Sathish Basker'),
    ('Umashree Ramesh', 'Umashree Ramesh'),
    ('Hariharan Alagesan', 'Hariharan Alagesan'),
    ('Prasanna Rohith', 'Prasanna Rohith'),
)
    engineer_empty = tuple(BLANK_CHOICE_DASH + list(engineer))
    NOC_Engineer = forms.ChoiceField(choices=(engineer_empty),widget=forms.Select(attrs={'id':'engid','onchange':'updateText("engid")','title':'The NOC Engineer who handled the incident','style': 'width: 55% !important; resize: vertical !important;'}))

    escalate=[('Yes','Yes'),('No','No')]
    #Escalated = forms.ChoiceField(choices=escalate, widget=forms.RadioSelect, initial='no')
    escalate_empty = tuple(BLANK_CHOICE_DASH + list(escalate))
    Escalated = forms.ChoiceField(choices=(escalate_empty), initial='No', widget=forms.Select(attrs={'title':'Was the alert escalated?','style': 'width: 55% !important; resize: vertical !important;'}))

    escreason = (
    ('Code level issue', 'Code level issue'),
    ('Configuration Changes', 'Configuration Changes'),
    ('Requesting Remediation', 'Requesting Remediation'),
    ('Unable to Resolve', 'Unable to Resolve'),
    ('Review Needed', 'Review Needed'),
    ('No Access', 'No Access'),
    ('NA', 'NA'),
)
    escreason_empty = tuple(BLANK_CHOICE_DASH + list(escreason))
    Escalated_Reason = forms.ChoiceField(choices=(escreason_empty), required=False, widget=forms.Select(attrs={'title':'The reson for escalation','style': 'width: 55% !important; resize: vertical !important;'}))

    stat = (
    ('Resolved', 'Resolved'),
    ('Pending', 'Pending'),
    ('Pending Followup', 'Pending Followup'),
    ('Handed over', 'Handed over')
    )
    stat_empty = tuple(BLANK_CHOICE_DASH + list(stat))
    Status = forms.ChoiceField(choices=(stat_empty),widget=forms.Select(attrs={'title':'Current status of the incident','style': 'width: 55% !important; resize: vertical !important;'}))

    escto = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    escto_empty = tuple(BLANK_CHOICE_DASH + list(escto))
    Escalated_to = forms.ChoiceField(choices=(escto_empty), required=False, widget=forms.Select(attrs={'title':'Enter the Team to whom the alert was escalated','style': 'width: 55% !important; resize: vertical !important;'}))

    resby = (
    ('B2B core', 'B2B core'),
    ('B2B reporting', 'B2B reporting'),
    ('B2B Data', 'B2B Data'),
    ('Beehive', 'Beehive'),
    ('BI', 'BI'),
    ('Data-Infra', 'Data-Infra'),
    ('Data-Prod', 'Data-Prod'),
    ('Data-Sci', 'Data-Sci'),
    ('Dev', 'Dev'),
    ('Dynamic Creative', 'Dynamic Creative'),
    ('Facebook', 'Facebook'),
    ('Growth', 'Growth'),
    ('GrowthIO', 'GrowthIO'),
    ('Internal tools', 'Internal tools'),
    ('IT', 'IT'),
    ('NA', 'NA'),
    ('NOC', 'NOC'),
    ('Omnom', 'Omnom'),
    ('Prospecting', 'Prospecting'),
    ('Rakuten', 'Rakuten'),
    ('RTB', 'RTB'),
    ('Sendroll', 'Sendroll'),
    ('SRE', 'SRE'),
    ('TAM', 'TAM'),
    ('Voltron', 'Voltron'),
    ('Webappp', 'Webappp'),
)
    resby_empty = tuple(BLANK_CHOICE_DASH + list(resby))
    Resolved_by_Team = forms.ChoiceField(choices=(resby_empty), widget=forms.Select(attrs={'title':'Enter the Team which resolved the alert','style': 'width: 55% !important; resize: vertical !important;'}))

    Resolved_by_Engineer = forms.CharField(widget=forms.TextInput(attrs={'id':'engidText','title':'The Engineer who resolved the alert','style': 'width: 55% !important; resize: vertical !important;'}))

    Description = forms.CharField(widget=forms.Textarea(attrs={'title':'Description of the alert','style': 'width: 55% !important; resize: vertical !important;'}))

    Remediation = forms.CharField(widget=forms.Textarea(attrs={'title':'Remediation done!','style': 'width: 55% !important; resize: vertical !important;'}))

    Resolution = forms.CharField(widget=forms.Textarea(attrs={'title':'Resolution!','style': 'width: 55% !important; resize: vertical !important;'}))

    Comments = forms.CharField(widget=forms.Textarea(attrs={'title':'Comments if any!','style': 'width: 55% !important; resize: vertical !important;'}))

    Host_Name = forms.CharField(widget=forms.TextInput(attrs={'title':'Host name of the alert','style': 'width: 55% !important; resize: vertical !important;'}))
    class Meta:
        model = models.Post
        field_order = ['Year','Week','Month','Date','Shift','Day_Of_Week','Time','Responded_Time','Time_spent','Complexity','Responsible_Team','False_alarm','Incident_Type','Priority','If_Others_Please_Specify','Description','Environment','Host_Type','Host_Name','Source_of_Alert','Mode_of_Alert','NOC_Engineer','Remediation','Escalated',
        'Escalated_Reason','Status','Escalated_to','Resolved_by_Team','Resolved_by_Engineer','Resolution','Comments']
        exclude = ['Ticket_Number','author']
