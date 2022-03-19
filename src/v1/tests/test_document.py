from rest_framework import status
from rest_framework.test import APITestCase
from .. import models
from .. import serializers


class DocumentTestCase(APITestCase):
    URL = '/v1/document/'

    def test_create_document(self):
        data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        res = self.client.post(self.URL, data)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        document = models.Document.objects.filter(title=data['title']).first()
        self.assertDictEqual(res.data, serializers.DocumentSerializer(
            document
        ).data)

    def test_retrieve_document(self):
        data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        models.Document.objects.create(**data)

        res = self.client.get(self.URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertListEqual(
            res.data, serializers.DocumentSerializer(
                models.Document.objects.all(), many=True
            ).data
        )

    def test_retrieve_document_by_id(self):
        data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        document = models.Document.objects.create(**data)

        res = self.client.get(f'{self.URL}{document.id}/')

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertDictEqual(res.data, serializers.DocumentSerializer(
            document
        ).data)

    def test_update_document_by_id(self):
        data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        document = models.Document.objects.create(**data)

        data['title'] = 'New Test'
        res = self.client.patch(f'{self.URL}{document.id}/', data)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

        document.refresh_from_db()
        self.assertDictEqual(res.data, serializers.DocumentSerializer(
            document
        ).data)

    def test_delete_document_by_id(self):
        data = {
            'title': 'Test',
            'content': 'This is the test content'
        }

        document = models.Document.objects.create(**data)

        res = self.client.delete(f'{self.URL}{document.id}/')

        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)


class FilterDocumentTestCase(APITestCase):
    URL = '/v1/document/'

    def setUp(self) -> None:
        self.folder1 = models.Folder.objects.create(name='Customer Feedback')
        self.folder2 = models.Folder.objects.create(name='Testimonials')

        self.doc1 = models.Document.objects.create(title='Client Feedback 1',
                                                   content='Love',
                                                   folder=self.folder1)
        self.doc2 = models.Document.objects.create(title='Client Feedback 2',
                                                   content='Hate',
                                                   folder=self.folder1)
        self.doc3 = models.Document.objects.create(title='Client Testimonial',
                                                   content='Testimonial',
                                                   folder=self.folder2)

        self.topic1 = models.Topic.objects.create(
            short_descriptor='SpekiLove!',
            long_descriptor='Positive feedback docs')
        self.topic2 = models.Topic.objects.create(
            short_descriptor='SpekiHate!',
            long_descriptor='Negative feedback docs')

        models.DocumentTopic.objects.create(document=self.doc1,
                                            topic=self.topic1)
        models.DocumentTopic.objects.create(document=self.doc2,
                                            topic=self.topic2)
        models.DocumentTopic.objects.create(document=self.doc3,
                                            topic=self.topic1)

    def test_retrieve_document_filter(self):
        res = self.client.get(self.URL, {
            'folder__name__icontains': 'Customer Feedback',
            'topics__short_descriptor__iexact': 'SpekiLove!'
        })

        expected_res = models.Document.objects.filter(
            folder__name__icontains='Customer Feedback',
            topics__short_descriptor__iexact='SpekiLove!'
        ).all()

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertListEqual(serializers.DocumentSerializer(
            expected_res, many=True
        ).data, res.data)
