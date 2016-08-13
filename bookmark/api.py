from bookmark.models import Bookmark, Folder
from bookmark.serializers import BookmarkSerializer, FolderSerializer
from rest_framework import viewsets
from rest_framework import filters
from rest_framework.exceptions import NotAuthenticated


class BookmarkViewSet(viewsets.ModelViewSet):

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    search_fields = ('title', 'description')
    filter_fields = ('folder',)


    def get_queryset(self):
        if self.request.user.is_anonymous():
            raise NotAuthenticated
        queryset = super(BookmarkViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class FolderViewSet(viewsets.ModelViewSet):

    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get_queryset(self):
        if self.request.user.is_anonymous():
            raise NotAuthenticated
        queryset = super(FolderViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)
