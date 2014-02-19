from django.conf.urls import patterns, url
from inventory_tracker import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^(?P<vehicle_id>\d+)/$', views.detail, name='detail'),
                       url(r'^(?P<vehicle_id>\d+)/mark_sold_by_me/$', views.mark_sold_by_me, name='mark_sold_by_me'),
                       )
