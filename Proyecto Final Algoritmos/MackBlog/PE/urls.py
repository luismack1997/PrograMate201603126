from django.conf.urls import url
from . import views
app_name='PE'

urlpatterns = [
    #/PE/
    url(r'^$', views.index, name='index'),
    #/PE/Problema36
    url(r'^Problema(?P<numero>[0-9]+)/$', views.detail, name='detail')
]