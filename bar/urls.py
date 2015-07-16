__author__ = 'yj'


from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^buy/(\d+)/$', views.buy, name='buy'),
    url(r'^buy/(\d+)/confirm$', views.confirm_buy, name='confirm_buy'),
]