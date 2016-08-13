from bookmark.models import Bookmark, Folder
from bookmark.serializers import BookmarkSerializer, FolderSerializer
from rest_framework import viewsets
from rest_framework import filters


class BookmarkViewSet(viewsets.ModelViewSet):

    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
    filter_backends = (filters.DjangoFilterBackend, filters.SearchFilter, )
    search_fields = ('title', 'description')
    filter_fields = ('folder',)


    def get_queryset(self):
        queryset = super(BookmarkViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)


class FolderViewSet(viewsets.ModelViewSet):

    queryset = Folder.objects.all()
    serializer_class = FolderSerializer

    def get_queryset(self):
        queryset = super(FolderViewSet, self).get_queryset()
        return queryset.filter(owner=self.request.user)
