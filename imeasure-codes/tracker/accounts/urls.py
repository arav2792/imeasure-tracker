from . import views
from django.conf.urls import url
from django.conf.urls import url, include
import accounts.views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

app_name = 'accounts'

urlpatterns = [
    url(r'^logout/', views.logoutview, name='logout'),
    url(r'^home/', views.homeview, name='home'),
    url(r'^forgot/', views.forgotview, name='forgot'),
    url(r'^usercreated/', views.usercreatedview, name='usercreated'),
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^password_changed/$', views.password_changed, name='password_changed'),
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
