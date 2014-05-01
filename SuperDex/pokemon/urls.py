from django.conf.urls import patterns, url

from pokemon import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)