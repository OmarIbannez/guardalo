from django.test import TestCase
from bookmark.models import Bookmark
from users.models import User
from unittest.mock import patch
from core.tests.test_utils import MockResponse


def mock_stackoverflow_response(*args, **kwargs):
    text = """<!DOCTYPE html>
    <html>
    <head>
        <title>Stack Overflow - Where Developers Learn, Share, &amp; Build Careers</title>
        <meta name="description" content="Stack Overflow is the largest, most trusted online community for developers to learn, share&#x200B; &#x200B;their programming &#x200B;knowledge, and build their careers."/>
        <meta property="og:type" content= "website" />
        <meta property="og:url" content="https://stackoverflow.com/"/>
        <meta property="og:site_name" content="Stack Overflow" />
        <meta property="og:image" itemprop="image primaryImageOfPage" content="https://cdn.sstatic.net/Sites/stackoverflow/Img/apple-touch-icon@2.png?v=73d79a89bded" />
        <meta name="twitter:card" content="summary"/>
        <meta name="twitter:domain" content="stackoverflow.com"/>
        <meta name="twitter:title" property="og:title" itemprop="name" content="Stack Overflow - Where Developers Learn, Share, &amp; Build Careers" />
        <meta name="twitter:description" property="og:description" itemprop="description" content="Stack Overflow | The World&#x2019;s Largest Online Community for Developers" />
    </head>
    <body class="home-page unified-theme"></body>"""
    return MockResponse(text=text)


class TestSaveBookmark(TestCase):

    def setUp(self):
        # Patch requests.get
        patcher = patch("requests.get")
        self.mock_call = patcher.start()
        self.addCleanup(patcher.stop)
        # Login
        user = User.objects.create(username="test_user")
        user.set_password("12345")
        user.save()
        self.client.login(username="test_user", password="12345")

    def test_save_bookmark_success(self):
        expected_title = "Stack Overflow - Where Developers Learn, " \
                         "Share, & Build Careers"
        expected_description = "Stack Overflow | The World’s " \
                               "Largest Online Community for Developers"
        self.mock_call.side_effect = mock_stackoverflow_response
        response = self.client.get("/{0}".format("https://stackoverflow.com"))
        bookmark = Bookmark.objects.first()
        self.assertEqual(1, Bookmark.objects.count())
        self.assertEqual(expected_title, bookmark.title)
        self.assertEqual(expected_description, bookmark.description)
        self.assertEquals(response.status_code, 302)

