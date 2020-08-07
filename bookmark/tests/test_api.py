import json

from django.test import TestCase
from bookmark.models import Folder
from users.models import User


class TestFolderViewSet(TestCase):
    def setUp(self):
        self.folder_api = "/bookmark/folder/api/"
        # Login
        self.user = User.objects.create(username="test_user")
        self.user.set_password("12345")
        self.user.save()
        self.client.login(username="test_user", password="12345")
        # Setup folders
        self.create_folders()
        self.folders = Folder.objects.all()

    def create_folders(self):
        for x in range(10):
            Folder.objects.create(name="Folder {0}".format(x), owner=self.user)

    def test_list_folders(self):
        response = self.client.get(self.folder_api)
        self.assertEquals(response.status_code, 200)
        self.assertEquals(len(response.data), len(self.folders))

    def test_get_folder(self):
        folder = self.folders[0]
        response = self.client.get("{}{}".format(self.folder_api, folder.id))
        self.assertEquals(response.data.get("name"), folder.name)

    def test_put_folder(self):
        folder = self.folders[0]
        new_folder_name = "New Folder Name"
        content_type = "application/json"
        payload = {
            "id": folder.id,
            "name": new_folder_name,
            "owner": folder.owner_id,
        }
        response = self.client.put(
            "{}{}".format(self.folder_api, folder.id),
            data=json.dumps(payload),
            content_type=content_type,
        )
        self.assertEquals(response.status_code, 200)
        self.assertEquals(response.data.get("name"), new_folder_name)

    def test_delete_folder(self):
        folder = self.folders[0]
        response = self.client.delete("{}{}".format(self.folder_api, folder.id))
        self.assertEquals(response.status_code, 204)
        response = self.client.get("{}{}".format(self.folder_api, folder.id))
        self.assertEqual(response.status_code, 404)
