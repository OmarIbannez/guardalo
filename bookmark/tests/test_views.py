from django.test import TestCase
from bookmark.models import Bookmark
from users.models import User
from unittest.mock import patch


class TestSaveBookmark(TestCase):
    def setUp(self):
        # Login
        user = User.objects.create(username="test_user")
        user.set_password("12345")
        user.save()
        self.client.login(username="test_user", password="12345")

    def test_save_bookmark_success(self):
        expected_title = "https://stackoverflow.com"
        expected_description = None
        response = self.client.get("/{0}".format("https://stackoverflow.com"))
        bookmark = Bookmark.objects.first()
        self.assertEqual(1, Bookmark.objects.count())
        self.assertEqual(expected_title, bookmark.title)
        self.assertEqual(expected_description, bookmark.description)
        self.assertEquals(response.status_code, 302)
