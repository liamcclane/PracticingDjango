from django.conf.urls import url
from . import views
                    
print('we are inside the urls function in dashboard')

urlpatterns = [
    url(r'^$', views.homePg),
    url(r'^book/(?P<id_book>\d+)$', views.bookDetails),
    url(r'^addBook$', views.addBook),
    url('/addAuthorToBook', views.addAuthorToBook),


    url(r'^author/(?P<id_author>\d+)$', views.authorDetails),
    url(r'^addAuthor$', views.addAuthor),
    url(r'^/addBookToAuthor', views.addBookToAuthor),
    url(r'^authors', views.showAuthors),
]