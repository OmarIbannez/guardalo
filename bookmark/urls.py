from django.conf.urls import url
from bookmark.api import BookmarkViewSet, FolderViewSet


""" API's URL's """
list_methods = {"get": "list", "post": "create"}

detail_methods = {
    "get": "retrieve",
    "patch": "update",
    "delete": "destroy",
    "put": "partial_update",
}

urlpatterns = [
    url(r"^api/$", BookmarkViewSet.as_view(list_methods), name="bookmark-list"),
    url(
        r"^api/(?P<pk>\d+)$",
        BookmarkViewSet.as_view(detail_methods),
        name="bookmark-detail",
    ),
    url(r"^folder/api/$", FolderViewSet.as_view(list_methods), name="folder-list"),
    url(
        r"^folder/api/(?P<pk>\d+)$",
        FolderViewSet.as_view(detail_methods),
        name="folder-detail",
    ),
]
