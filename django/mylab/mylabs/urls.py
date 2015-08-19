from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^led/$', views.led_page, name='led_page'),
    url(r'^led/(?P<bool>[-\w]+)/$', views.led_page, name='led_page'),
    url(r'^led/(?P<pin>\d+)/(?P<bool>[-\w]+)/$', views.led_page, name='led_page'),
    url(r'^ultrasonido/$', views.ultra_page, name='ultra_page'),
    url(r'^ultrasonido/(?P<bool>[-\w]+)/$', views.ultra_page, name='ultra_page'),
    url(r'^get-ultra/$', views.get_ultrasonido, name='get_ultrasonido'),
    url(r'^luz/$', views.luz_page, name='luz_page'),
    url(r'^luz/(?P<pin>\d+)/(?P<bool>[-\w]+)/$', views.luz_page, name='luz_page'),
    url(r'^luz/(?P<bool>[-\w]+)/$', views.luz_page, name='luz_page'),
    

]

