from django.conf.urls import url
from . import views
                    
print('we are inside the urls function inside dashboard')

urlpatterns = [
    url(r'^$', views.homePg),
    url(r'^process_money$', views.moneyProcess),
    url(r'^destroy$', views.reset),
]