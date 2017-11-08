from django.conf.urls import url
from PROYECTO_APP import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^orden/nueva/$', views.orden_nueva, name='orden_nueva'),
    url(r'^ordenes/$', views.ordenes, name='ordenes'),
    url(r'^orden/(?P<pk>[0-9]+)/editar/$', views.orden_edit, name='orden_edit'),
    url(r'^orden/(?P<pk>[0-9]+)/eliminar/$', views.orden_delete, name='orden_delete'),

    #url(r'^material/(?P<pk>[0-9]+)/editar/$', views.material_edit, name='material_edit'),
    url(r'^material/nuevo/$', views.nuevo_material, name='nuevo_material'),
    url(r'^materiales$', views.materiales, name='materiales'),
    url(r'^material/(?P<pk>[0-9]+)/editar/$', views.material_edit, name='material_edit'),
    url(r'^material/(?P<pk>[0-9]+)/eliminar/$', views.material_delete, name='material_delete'),
    ]
