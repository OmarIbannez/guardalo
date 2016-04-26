from __future__ import unicode_literals
from django.db import models
from core.models import BaseModel
from django.conf import settings


class Folder(BaseModel):
    name = models.CharField(max_length=255)

    def __unicode__(self):
        return u'{0}'.format(self.name)

    def __str__(self):
        return self.__unicode__()


class Bookmark(BaseModel):

    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    thumbnail = models.URLField(null=True, blank=True)
    folder = models.ForeignKey(Folder, null=True, blank=True)

    def __unicode__(self):
        return u'{0}'.format(self.title)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        pass
