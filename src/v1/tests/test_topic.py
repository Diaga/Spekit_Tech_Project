from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class TopicTestCase(APITestCase):
    URL = '/v1/topic/'

    def test_create_topic(self):
        data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        res = self.client.post(self.URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        topic = models.Topic.objects.filter(
            short_descriptor=data['short_descriptor']).first()
        self.assertDictEqual(res.data, serializers.TopicSerializer(
            topic
        ).data)

    def test_retrieve_topic(self):
        data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        models.Topic.objects.create(**data)

        res = self.client.get(self.URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertListEqual(res.data, serializers.TopicSerializer(
            models.Topic.objects.all(), many=True
        ).data)

    def test_retrieve_topic_by_id(self):
        data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        topic = models.Topic.objects.create(**data)

        res = self.client.get(f'{self.URL}{topic.id}/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(res.data, serializers.TopicSerializer(
            topic
        ).data)

    def test_update_topic_by_id(self):
        data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        topic = models.Topic.objects.create(**data)

        data['short_descriptor'] = 'new_support'

        res = self.client.patch(f'{self.URL}{topic.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        topic.refresh_from_db()
        self.assertDictEqual(
            res.data, serializers.TopicSerializer(
                topic
            ).data
        )

    def test_delete_topic_by_id(self):
        data = {
            'short_descriptor': 'support',
            'long_descriptor': 'support for developers'
        }

        topic = models.Topic.objects.create(**data)

        res = self.client.delete(f'{self.URL}{topic.id}/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
