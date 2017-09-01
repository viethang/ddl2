from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<sciper>[0-9]+)/$', views.details, name = 'details')
]