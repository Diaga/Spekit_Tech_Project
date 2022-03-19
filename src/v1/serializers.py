from rest_framework.serializers import ModelSerializer
from . import models


class TopicSerializer(ModelSerializer):
    class Meta:
        model = models.Topic
        fields = ('id', 'short_descriptor', 'long_descriptor')


class FolderSerializer(ModelSerializer):
    class Meta:
        model = models.Folder
        fields = ('id', 'name', 'folder', 'topics')


class DocumentSerializer(ModelSerializer):
    class Meta:
        model = models.Document
        fields = ('id', 'title', 'content', 'folder', 'topics')


class FolderTopicSerializer(ModelSerializer):
    class Meta:
        model = models.FolderTopic
        fields = ('id', 'folder', 'topic')


class DocumentTopicSerializer(ModelSerializer):
    class Meta:
        model = models.DocumentTopic
        fields = ('id', 'document', 'topic')
