from django.test import TestCase
from unittest.mock import patch
from core.tests.test_utils import MockResponse
from bookmark.link import Link


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


class TestLink(TestCase):
    def setUp(self):
        # Patch requests.get
        patcher = patch("requests.get")
        self.mock_call = patcher.start()
        self.addCleanup(patcher.stop)

    def test_fetch_link(self):
        expected_title = (
            "Stack Overflow - Where Developers Learn, Share, & Build Careers"
        )
        expected_description = (
            "Stack Overflow | The World’s Largest Online Community for Developers"
        )
        self.mock_call.side_effect = mock_stackoverflow_response
        link = Link(url="https://stackoverflow.com")
        link.fetch()
        self.assertEqual(expected_title, link.title)
        self.assertEqual(expected_description, link.description)
