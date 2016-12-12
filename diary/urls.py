from django.conf.urls import url

from . import views

app_name = 'diary'

app_name = 'diary'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<qst>[0-9]+)/base/$', views.base, name='base'),
]
