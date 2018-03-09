# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

app_name = 'usuario'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    # usuarioi/registro
    url(r'^registro/$', views.UsuarioCreate.as_view(), name='registro'),
    # usuario/ingreso
    url(r'^ingreso/$', views.LogIn.as_view(), name='ingreso'),
    # página del usuario modificar
    url(r'(?P<pk>.+)/modificar/', views.UsuarioUpdate.as_view(success_url='/usuario/'), name='usuarioEditar'),
    # info usuario
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',views.activate, name='activate'),
    url(r'^(?P<Usuario>.+)/', views.detail, name='detail'),
    
]
