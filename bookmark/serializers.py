from rest_framework import serializers
from bookmark.models import Bookmark, Folder


class BookmarkSerializer(serializers.ModelSerializer):
    thumbnail = serializers.SerializerMethodField()
    folder_name = serializers.SerializerMethodField()

    class Meta:
        model = Bookmark
        fields = (
            "id",
            "url",
            "title",
            "description",
            "thumbnail",
            "owner",
            "folder",
            "folder_name",
        )

    def get_thumbnail(self, obj):
        if not obj.thumbnail:
            return "/static/img/default.jpg"
        return obj.thumbnail

    def get_folder_name(self, obj):
        if obj.folder:
            return obj.folder.name


class FolderSerializer(serializers.ModelSerializer):
    owner = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Folder
        fields = ("id", "name", "owner")

    def create(self, validated_data):
        validated_data["owner"] = self.context["request"].user
        return super(FolderSerializer, self).create(validated_data)
