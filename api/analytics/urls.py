from django.conf.urls import url

from . import views

app_name ='analytics'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<sciper>[0-9]+)/$', views.detail, name='detail')
]
