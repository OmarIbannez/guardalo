from django.db import models
from core.models import BaseModel


class Folder(BaseModel):

    name = models.CharField(max_length=255)

    def __str__(self):
        return "{0}".format(self.name)


class Bookmark(BaseModel):

    url = models.URLField(max_length=1000)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True, max_length=1000)
    folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return "{0}".format(self.title)

    class Meta:
        ordering = ("-created_at",)
