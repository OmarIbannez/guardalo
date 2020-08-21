import kronos
from .link import Link
from .models import Bookmark


def fetch_bookmark_details():
    bookmarks = Bookmark.objects.filter(fetched=False, connection_error=False)
    for bookmark in bookmarks:
        link = Link(url=bookmark.url)
        link.fetch()
        if link.is_invalid:
            bookmark.connection_error = True
            bookmark.save()
            continue
        bookmark.title = link.title
        bookmark.description = link.description
        bookmark.thumbnail = link.image
        bookmark.save()


@kronos.register("* * * * *")
def cron_fetch_bookmark_details():
    fetch_bookmark_details()
