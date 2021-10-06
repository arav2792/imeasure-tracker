from django.contrib import admin
from django.conf.urls import url, include
import accounts.views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.conf.urls import *
from accounts import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls')),
    url(r'^posts/', include('posts.urls')),
    url(r'^updates/', include('updates.urls')),
    #url(r'^devops/', include('devops.urls')),
    url(r'^$', views.loginview, name="login")
]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
