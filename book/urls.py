from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('admin_page', views.admin_view, name='admin_page'),
    path('add_book', views.add_book, name='add_book'),
    path('add_author', views.add_author, name='add_author'),
    path('ajax_test', views.ajax_test, name='ajax_test'),
    path('book_search', views.book_search, name='book_search'),
]

