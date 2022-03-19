from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'topic', views.TopicViewSet)
router.register(r'folder', views.FolderViewSet)
router.register(r'document', views.DocumentViewSet)
router.register(r'm2m/folder/topic', views.FolderTopicViewSet)
router.register(r'm2m/document/topic', views.DocumentTopicViewSet)

urlpatterns = router.urls
