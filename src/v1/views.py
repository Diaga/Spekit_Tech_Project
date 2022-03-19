from rest_framework.viewsets import GenericViewSet, mixins

from . import models
from . import serializers
from . import filters


class TopicViewSet(GenericViewSet,
                   mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.ListModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin):
    queryset = models.Topic.objects.all()
    serializer_class = serializers.TopicSerializer


class FolderViewSet(GenericViewSet,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    queryset = models.Folder.objects.all()
    serializer_class = serializers.FolderSerializer
    filterset_class = filters.FolderFilter


class DocumentViewSet(GenericViewSet,
                      mixins.CreateModelMixin,
                      mixins.RetrieveModelMixin,
                      mixins.ListModelMixin,
                      mixins.UpdateModelMixin,
                      mixins.DestroyModelMixin):
    queryset = models.Document.objects.all()
    serializer_class = serializers.DocumentSerializer
    filterset_class = filters.DocumentFilter


class FolderTopicViewSet(GenericViewSet,
                         mixins.CreateModelMixin,
                         mixins.DestroyModelMixin):
    queryset = models.FolderTopic.objects.all()
    serializer_class = serializers.FolderTopicSerializer


class DocumentTopicViewSet(GenericViewSet,
                           mixins.CreateModelMixin,
                           mixins.DestroyModelMixin):
    queryset = models.DocumentTopic.objects.all()
    serializer_class = serializers.DocumentTopicSerializer
