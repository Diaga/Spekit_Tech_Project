from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class FolderTopicTestCase(APITestCase):
    URL = '/v1/m2m/folder/topic/'
    FOLDER_URL = '/v1/folder/'

    def test_create_folder_topic(self):
        topic_data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        folder_data = {
            'name': 'Test'
        }

        folder = models.Folder.objects.create(**folder_data)
        topic = models.Topic.objects.create(**topic_data)

        data = {
            'folder': str(folder.id),
            'topic': str(topic.id)
        }
        res = self.client.post(self.URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        folder_topic = models.FolderTopic.objects.filter(
            folder__id=data['folder']
        ).first()
        self.assertDictEqual(res.data, serializers.FolderTopicSerializer(
            folder_topic
        ).data)

        res_folder = self.client.get(f'{self.FOLDER_URL}{folder.id}/')
        self.assertIn(topic.id, res_folder.data['topics'])

    def test_delete_folder_topic(self):
        topic_data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        folder_data = {
            'name': 'Test'
        }

        folder = models.Folder.objects.create(**folder_data)
        topic = models.Topic.objects.create(**topic_data)

        data = {
            'folder': folder,
            'topic': topic
        }

        folder_topic = models.FolderTopic.objects.create(**data)

        res = self.client.delete(f'{self.URL}{folder_topic.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res_folder = self.client.get(f'{self.FOLDER_URL}{folder.id}/')
        self.assertNotIn(topic.id, res_folder.data['topics'])
