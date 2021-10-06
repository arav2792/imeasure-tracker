from . import views
from django.conf.urls import url
from urllib.parse import unquote
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
app_name = 'posts'

urlpatterns = [
    url(r'^quicklinks/', views.quicklinkview, name='quicklinks'),
    url(r'^tracker_list/', views.tracker_list, name='tracker_list'),
    url(r'^(?P<track_id>[0-9]+)/$', views.tracker_view, name="tracker_view"),
    url(r'^tracker_edit/', views.tracker_edit, {}, name='tracker_edit'),
    url(r'^modify/(?P<track_id>[0-9]+)/$', views.tracker_edit, {}, name='modify'),
    url(r'^search/$', views.search, name='search'),
    url(r'^pending/', views.pending, name='pending'),
    url(r'^unattended/', views.unattended, name='unattended'),
    url(r'^schedule/', views.schedule, name='schedule'),
]  + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
