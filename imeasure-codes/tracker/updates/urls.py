from . import views
from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static

app_name = 'updates'

urlpatterns = [
    url(r'^modify/(?P<up_id>[0-9]+)/$', views.process_updates, {}, name='modify'),
    url(r'^process_updates/', views.process_updates, {}, name='process_updates'),
    url(r'^updates_list/', views.updates_list, name='updates_list'),
    url(r'^(?P<up_id>[0-9]+)/$', views.update_view, name="update_view"),
]
