from rest_framework import serializers
from bookmark.models import Bookmark, Folder


class BookmarkSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()

    class Meta:
        model = Bookmark
        fields = (
            'id',
            'url',
            'title',
            'description',
            'thumbnail',
            'owner'
        )

    def get_thumbnail(self, obj):
            if not obj.thumbnail:
                return '/static/img/default.jpg'
            return obj.thumbnail


class FolderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Folder
        fields = (
            'id',
            'name'
        )
