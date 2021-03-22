from rest_framework.urlpatterns import format_suffix_patterns

from Book.views import *
from rest_framework import renderers
from django.urls import path, include
Author_list = AuthorViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
Author_detail = AuthorViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})
# Author_highlight = AuthorViewSet.as_view({
#     'get': 'highlight'
# })

urlpatterns = format_suffix_patterns([
    path('', api_root),
    path('Author/', Author_list, name='books-list'),
    path('Author/<int:pk>/', Author_detail, name='books-detail'),
    # path('Author/<int:pk>/books/', Author_highlight, name='Author-books'),
    path('BookCreate/',BookCreateView.as_view(),name='book-list'),
    path('BookRetrieveUpdateDestroy/<int:pk>',BookRetrieveUpdateDestroyView.as_view(),name='book_detail'),
    # path('BookUpdate/<int:pk>',BookUpdateView.as_view(),name='book_pat'),
    path('BookAuthorSearchList/',BookAuthorSearchList.as_view(),name='book_asl'),

])
# }), renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })


