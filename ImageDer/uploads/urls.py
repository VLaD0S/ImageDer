from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.upload_home, name='home'),
    url(r'^create/$', views.upload_create, name='create'),
    url(r'^detail/$', views.upload_detail, name='detail'),
    url(r'^list/$', views.upload_list, name='list'),
    url(r'^delete/$', views.upload_delete, name='delete'),

]