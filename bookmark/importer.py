from bs4 import BeautifulSoup


class Bookmark:
    def __init__(self, title, url, folder):
        self.title = title
        self.url = url
        self.folder = folder

    def __str__(self):
        return self.title + " " + self.url + " " + self.folder


class HtmlBookmarks:
    def __init__(self, html):
        self.soup = BeautifulSoup(html, "html.parser")

    def parse(self):
        html_tags = self.soup.findAll(["h3", "a"])
        folder = ""

        for tag in html_tags:
            if tag.name == "h3":
                folder = tag.string
            if tag.name == "a":
                yield Bookmark(tag.string, tag["href"], folder)
