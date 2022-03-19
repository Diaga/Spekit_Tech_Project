from django_filters import rest_framework as filters
from . import models


class DocumentFilter(filters.FilterSet):
    class Meta:
        model = models.Document
        fields = {
            'title': ['iexact', 'icontains'],
            'folder__name': ['iexact', 'icontains'],
            'topics__short_descriptor': ['iexact', 'icontains'],
            'topics__long_descriptor': ['iexact', 'icontains']
        }


class FolderFilter(filters.FilterSet):
    class Meta:
        model = models.Folder
        fields = {
            'name': ['iexact', 'icontains'],
            'folder__name': ['iexact', 'icontains'],
            'topics__short_descriptor': ['iexact', 'icontains'],
            'topics__long_descriptor': ['iexact', 'icontains']
        }
