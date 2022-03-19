from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class DocumentTopicTestCase(APITestCase):
    URL = '/v1/m2m/document/topic/'
    DOCUMENT_URL = '/v1/document/'

    def test_create_document_topic(self):
        topic_data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        document_data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        document = models.Document.objects.create(**document_data)
        topic = models.Topic.objects.create(**topic_data)

        data = {
            'document': str(document.id),
            'topic': str(topic.id)
        }
        res = self.client.post(self.URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        document_topic = models.DocumentTopic.objects.filter(
            document__id=data['document']
        ).first()
        self.assertDictEqual(res.data, serializers.DocumentTopicSerializer(
            document_topic
        ).data)

        res_document = self.client.get(f'{self.DOCUMENT_URL}{document.id}/')
        self.assertIn(topic.id, res_document.data['topics'])

    def test_delete_document_topic(self):
        topic_data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        document_data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        document = models.Document.objects.create(**document_data)
        topic = models.Topic.objects.create(**topic_data)

        data = {
            'document': document,
            'topic': topic
        }

        document_topic = models.DocumentTopic.objects.create(**data)

        res = self.client.delete(f'{self.URL}{document_topic.id}/')
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)

        res_document = self.client.get(f'{self.DOCUMENT_URL}{document.id}/')
        self.assertNotIn(topic.id, res_document.data['topics'])
