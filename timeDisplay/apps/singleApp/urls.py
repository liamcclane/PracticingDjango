from django.conf.urls import url
from . import views
                    
print('we are inside the urls function in urls app only')

urlpatterns = [
    url(r'^$', views.homePg),
    url(r'^/time$', views.index),
]