from django.conf.urls import include, url
from django.contrib import admin

from polls import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^polls/', include('polls.urls')),
    url(r'^diary/', include('diary.urls')),
]
