__author__ = 'yj'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buy/(\d+)/$', views.buy, name='buy'),
]