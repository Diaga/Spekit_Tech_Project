from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class FolderTestCase(APITestCase):
    URL = '/v1/folder/'

    def test_create_folder(self):
        data = {
            'name': 'Test'
        }

        res = self.client.post(self.URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        folder = models.Folder.objects.filter(name=data['name']).first()
        self.assertDictEqual(res.data, serializers.FolderSerializer(
            folder
        ).data)

    def test_retrieve_folder(self):
        data = {
            'name': 'Test'
        }

        models.Folder.objects.create(**data)

        res = self.client.get(self.URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            res.data, serializers.FolderSerializer(
                models.Folder.objects.all(), many=True
            ).data
        )

    def test_retrieve_folder_by_id(self):
        data = {
            'name': 'Test'
        }

        folder = models.Folder.objects.create(**data)

        res = self.client.get(f'{self.URL}{folder.id}/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(res.data, serializers.FolderSerializer(
            folder
        ).data)

    def test_update_folder_by_id(self):
        data = {
            'name': 'Test'
        }

        folder = models.Folder.objects.create(**data)

        data['name'] = 'New Test'
        res = self.client.patch(f'{self.URL}{folder.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        folder.refresh_from_db()
        self.assertDictEqual(res.data, serializers.FolderSerializer(
            folder
        ).data)

    def test_delete_folder_by_id(self):
        data = {
            'name': 'Test'
        }

        folder = models.Folder.objects.create(**data)

        res = self.client.delete(f'{self.URL}{folder.id}/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class FilterFolderTestCase(APITestCase):
    URL = '/v1/folder/'

    def setUp(self) -> None:
        self.folder1 = models.Folder.objects.create(name='Customer Feedback')
        self.folder2 = models.Folder.objects.create(name='Testimonials',
                                                    folder=self.folder1)
        self.folder3 = models.Folder.objects.create(name='API Routes',
                                                    folder=self.folder1)

        self.topic1 = models.Topic.objects.create(
            short_descriptor='SpekiLove!',
            long_descriptor='Positive feedback docs')
        self.topic2 = models.Topic.objects.create(
            short_descriptor='SpekiHate!',
            long_descriptor='Negative feedback docs')

        models.FolderTopic.objects.create(folder=self.folder1,
                                          topic=self.topic1)
        models.FolderTopic.objects.create(folder=self.folder1,
                                          topic=self.topic2)
        models.FolderTopic.objects.create(folder=self.folder2,
                                          topic=self.topic1)

    def test_retrieve_folder_filter(self):
        res = self.client.get(self.URL, {
            'folder__name__icontains': 'Customer Feedback',
            'topics__short_descriptor__iexact': 'SpekiLove!'
        })

        expected_res = models.Folder.objects.filter(
            folder__name__icontains='Customer Feedback',
            topics__short_descriptor__iexact='SpekiLove!'
        ).all()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertListEqual(serializers.FolderSerializer(
            expected_res, many=True
        ).data, res.data)
