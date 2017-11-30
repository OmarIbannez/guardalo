from django.views.generic import View
from bookmark.link import Link
from bookmark.models import Bookmark as BookmarkModel
from django.views.generic import TemplateView
from django.shortcuts import redirect
from django.conf import settings


class SaveBookmark(View):

    def get(self, request, url):
        url = request.get_full_path()[1:]
        try:
            link = Link(url=url)
        except Exception as e:
            return redirect(settings.LOGIN_REDIRECT_URL)

        title = link.title or link.url
        bookmark = BookmarkModel(
            url=link.url,
            title=title[:255],
            description=link.description,
            thumbnail=link.image,
            owner=self.request.user
        )
        bookmark.save()

        return redirect(settings.LOGIN_REDIRECT_URL)


class Bookmark(TemplateView):
    template_name = 'bookmarks/list.html'
