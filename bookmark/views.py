from django.views.generic import View
from bookmark.models import Bookmark as BookmarkModel
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings


class SaveBookmark(View):
    def get(self, request, url):
        url = request.get_full_path()[1:]
        title = url
        bookmark = BookmarkModel(url=url, title=title[:255], owner=self.request.user)
        bookmark.save()

        return redirect(settings.LOGIN_REDIRECT_URL)


class Bookmark(TemplateView):
    template_name = "bookmarks/list.html"
