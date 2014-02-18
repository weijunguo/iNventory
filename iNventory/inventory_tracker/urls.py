from django.conf.urls import patterns, url
from inventory_tracker import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<vehicle_id>\d+)/$', views.detail, name='detail'),
                       )
