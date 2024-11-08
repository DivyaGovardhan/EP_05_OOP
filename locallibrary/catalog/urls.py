from django.urls import include
from django.urls import path
from . import views
from django.conf.urls import url
from .views import MyView

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^books/$', views.BookListView.as_view(), name='books'),
    url(r'^book/(?P<pk>\d+)/$', views.BookDetailView.as_view(), name='book-detail'),
    url(r'^author/$', views.AuthorListView.as_view(), name='authors'),
    url(r'^author/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name='author-detail'),
    path('my-view/', MyView.as_view(), name='my_view'),
    url(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
