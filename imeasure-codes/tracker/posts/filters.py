from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from . import models
from django_tables2.utils import A
from . import views
from django.contrib.auth.models import User
import django_filters
from distutils.util import strtobool

BOOLEAN_CHOICES = (('false', 'False'), ('true', 'True'),)

class TrackerFilter(django_filters.FilterSet):
    #Date = django_filters.TypedMultipleChoiceFilter(choices=BOOLEAN_CHOICES,coerce=strtobool)
    class Meta:
        model = models.Post
        fields = '__all__'
        #fields = ['Status']

class PendingFilter(django_filters.FilterSet):
    class Meta:
        model = models.Post
        #fields = '__all__'
        fields = ['Status']

class UnattendedFilter(django_filters.FilterSet):
    class Meta:
        model = models.Post
        #fields = '__all__'
        fields = ['Resolved_by_Engineer']
