from rest_framework.routers import DefaultRouter
from doc_manager_app.views import DocumentsViewSet, FoldersViewSet, TopicsViewSet, TopicAssociationViewSet

doc_manager = DefaultRouter()

doc_manager.register(r'folder', FoldersViewSet, 'folder')
doc_manager.register(r'document', DocumentsViewSet, 'document')
doc_manager.register(r'topic', TopicsViewSet, 'topic')
doc_manager.register(r'topic_association', TopicAssociationViewSet, 'topic')
