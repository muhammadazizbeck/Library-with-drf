from django.urls import path
from . import views

urlpatterns = [
    # path('books/',views.BookListApiView.as_view(),name='book_list'),
    # path('books/create/',views.BookCreateApiView.as_view(),name='book_create'),
    # path('booklc',views.BookListCreateApiView.as_view(),name='book-list-create'),
    # path('books/<int:pk>/',views.BookDetailApiView.as_view(),name='book_detail'),
    # path('books/<int:pk>/update/',views.BookUpdateApiView.as_view(),name='book_update'),
    # path('books/<int:pk>/delete/',views.BookDeleteApiView.as_view(),name='book_delete')
    path('books/',views.BookListApiView.as_view(),name='book-list'),
    path('books/create/',views.BookCreateApiView.as_view(),name='book-create'),
    path('books/<int:pk>/',views.BookDetailApiView.as_view(),name='book-detail'),
    path('books/<int:pk>/delete/',views.BookDeleteApiView.as_view(),name='book-delete'),
    path('books/<int:pk>/update/',views.BookUpdateApiView.as_view(),name='book-update'),
    # path('bookrud<int:pk>/',views.BookRetrieveUpdateDestroyApiView.as_view(),name='book-retrieve-update-delete')
]