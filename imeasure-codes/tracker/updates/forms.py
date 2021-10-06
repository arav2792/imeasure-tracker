from django import forms
from django.contrib.auth.models import User
from django.utils import timezone
import datetime
from . import models
from django.utils.safestring import mark_safe
from django.forms import widgets
import datetime
from django.db.models.fields import BLANK_CHOICE_DASH


class UpdateArticle(forms.ModelForm):

    status=[('Active','Active'),('Old','Old')]
    Status = forms.ChoiceField(choices=status, widget=forms.RadioSelect, initial='Active')

    class Meta:
        model = models.Update
        fields = '__all__'
        field_order = ['Date','Topic','From','Description','Status']
