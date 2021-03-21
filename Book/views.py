from rest_framework import permissions
from rest_framework import viewsets
from rest_framework.authentication import *
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView, CreateAPIView
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.reverse import reverse
from Book.serializers import *
from rest_framework import filters
from rest_framework import generics
from UserLog.views import *
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Author': reverse('Author-list', request=request, format=format)
    })
class AuthorViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Author.objects.all()
    # serializer_class = AuthorSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [permissions.IsAdminUser]

    # def get_queryset(self):
    #     return self.request.user.accounts.all()
    # @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    # def books(self, request, *args, **kwargs):
    #     author = self.get_object()
    #     return Response(author.books)
    # def check_object_permissions(self, request, obj):
    serializer_classes = {
        'list': AuthorListSerializer,
        'retrieve': AuthorDetailSerializer,
        # ... other actions
    }
    default_serializer_class = AuthorSerializer

    def get_serializer_class(self):
        return self.serializer_classes.get(self.action, self.default_serializer_class)
    def get_permissions(self):
        """
        Instantiates and returns the list of permissions that this view requires.
        """
        if self.action == 'list':
            permission_classes = [permissions.IsAuthenticatedOrReadOnly]
        else:
            permission_classes = [permissions.IsAdminUser]
        return [permission() for permission in permission_classes]
    def perform_create(self, serializer):
        permission_classes = permissions
        serializer.save()
class BookCreateView(ListCreateAPIView):
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get_queryset(self):
        # last_two_days = now() - timedelta(days=2)
        return Book.objects.all()
    def get_serializer_class(self):
        if self.request.method == 'GET':
            return BookSerializer1


class BookRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    # serializer_class = BookSerializer
    # serializer_class1=BookSerializer1
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAdminUser]

    def get_serializer_class(self):
        if self.request.method == 'PATCH':
            return BookSerializer1
        else:
            return BookSerializer

    #     # return self.serializer_classes.get(self.action, self.default_serializer_class)
    # # def get_serializer(self):
    #     """
    #     Instantiates and returns the list of permissions that this view requires.
    #     """
    #     if self.request == 'patch':
    #         serializer_class = BookSerializer1
    #     # else:
    #     #     permission_classes = [permissions.IsAdminUser]
    #     return self.serializer_class.get(self.action, self.default_serializer_class)
        # return [permission() for permission in permission_classes]
    # def get_serializer(self, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return super(BookSerializer1, self).get_serializer(*args, **kwargs)
    # def patch(self, request, *args, **kwargs):
    #     kwargs['partial'] = True
    #     return self.update(request, *args, **kwargs)
    # def patch(self, request, *args, **kwargs):
    #     kwargs['partial'] = False
    #     return self.update(request, *args, **kwargs)
class DynamicSearchFilter(filters.SearchFilter):
    def get_search_fields(self, view, request):
        return request.GET.getlist('search_fields', [])
class BookAuthorSearchList(ListAPIView):
    search_fields = ['author__name','name','rating','description','author__age','isbn']
    filter_backends = (filters.SearchFilter,DynamicSearchFilter,)
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    authentication_classes = [TokenAuthentication,SessionAuthentication]
    permission_classes = [IsAuthenticated]
# class BookListView(ListAPIView):
#     search_fields = ['author','book_name']
#     filter_backends = (filters.SearchFilter,)
#     queryset = Books.objects.all()
#     serializer_class = BookSerializer
#     authentication_classes = [BasicAuthentication]
#     permission_classes = [IsAuthenticated]