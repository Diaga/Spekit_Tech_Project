from django.db import models
from uuid import uuid4


class Topic(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    short_descriptor = models.CharField(max_length=255, blank=False,
                                        unique=True)
    long_descriptor = models.TextField(blank=False)

    class Meta:
        app_label = 'v1'
        default_related_name = 'topics'

    def __str__(self):
        return self.short_descriptor


class Folder(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    name = models.CharField(max_length=255, blank=False)

    folder = models.ForeignKey('Folder', on_delete=models.CASCADE, null=True)

    topics = models.ManyToManyField(
        Topic,
        through='FolderTopic',
        through_fields=('folder', 'topic')
    )

    class Meta:
        app_label = 'v1'
        default_related_name = 'folders'

    def __str__(self):
        return self.name


class Document(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)
    title = models.CharField(max_length=255, default='Untitled Document',
                             blank=False)
    content = models.TextField(blank=True)

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)

    topics = models.ManyToManyField(
        Topic,
        through='DocumentTopic',
        through_fields=('document', 'topic')
    )

    class Meta:
        app_label = 'v1'
        default_related_name = 'documents'

    def __str__(self):
        return f'{self.title} - {self.folder}'


class FolderTopic(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        app_label = 'v1'
        default_related_name = 'folder_topics'

    def __str__(self):
        return f'{self.folder} - {self.topic}'


class DocumentTopic(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid4)

    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)

    class Meta:
        app_label = 'v1'
        default_related_name = 'document_topics'

    def __str__(self):
        return f'{self.document} - {self.topic}'
