from django.conf.urls import url
from . import views
                    
print('we are inside the urls function in apps in rnd_wold folder')

urlpatterns = [
    url(r'^$', views.index),
    url(r'^/generate$', views.generateFun),
    url(r'^/destroy$', views.destroyFun),
]