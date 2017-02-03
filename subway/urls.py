from django.conf.urls import url, include
from .views import SubwayLV, subway_lazy, subway_now,main,bsbusy,bsempty

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'busy/$', SubwayLV, name='busy'),
    url(r'lazy/$', subway_lazy, name='lazy'),
    url(r'now/$', subway_now, name='now'),

    url(r'1bz/$', bsbusy, name='1bz'),
    url(r'2em/$', bsempty, name='2em'),

]
