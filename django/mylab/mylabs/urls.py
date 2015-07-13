from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^led/$', views.led_page, name='led_page'),
    url(r'^led/(?P<bool>[-\w]+)/$', views.led_page, name='led_page'),
    url(r'^led/(?P<pin>\d+)/(?P<bool>[-\w]+)/$', views.led_page, name='led_page'),

]

