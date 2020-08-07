from django.views.generic import View
from django.db import DatabaseError
from bookmark.models import Bookmark as BookmarkModel, Folder
from django.views.generic import TemplateView
from django.http import HttpResponse
from bookmark.importer import HtmlBookmarks
import json


class ImportBookmarks(View):
    def post(self, request):
        if not request.FILES:
            message = "Select a correct HTML file"
            response = json.dumps({"False": True, "message": message})
            return HttpResponse(response)
        f = request.FILES["file"]
        html = ""
        for chunk in f.chunks():
            html += str(chunk)
        bookmarks = HtmlBookmarks(html)
        for bookmark in bookmarks.parse():
            folder = None
            if bookmark.folder:
                try:
                    folder = Folder.objects.get(
                        name=bookmark.folder, owner=self.request.user
                    )
                except Folder.DoesNotExist:
                    folder = Folder(name=bookmark.folder, owner=self.request.user)
                    folder.save()
            mark = BookmarkModel(
                url=bookmark.url,
                title=bookmark.title or bookmark.url,
                owner=self.request.user,
                folder=folder,
            )
            try:
                mark.save()
            except DatabaseError:
                message = "Opps, Something fail."
                response = json.dumps({"False": True, "message": message})
                return HttpResponse(response)
        message = "Bookmarks saved successfully"
        response = json.dumps({"status": True, "message": message})
        return HttpResponse(response)


class SettingsView(TemplateView):
    template_name = "settings/index.html"
