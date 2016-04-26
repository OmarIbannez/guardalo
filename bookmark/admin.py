from django.contrib import admin
from bookmark.models import Bookmark, Folder


admin.site.register(Bookmark)
admin.site.register(Folder)
