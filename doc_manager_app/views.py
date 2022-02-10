from rest_framework import mixins
from rest_framework.viewsets import GenericViewSet
from doc_manager_app.models import Folder, Document, Topic, TopicAssociation
from doc_manager_app.serializers import FoldersSerializer, DocumentsSerializer, TopicsSerializer, \
    FoldersDetailSerializer, DocumentsDetailSerializer, TopicAssociationSerializer
from rest_framework.response import Response


class FoldersViewSet(mixins.ListModelMixin,
                     mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.UpdateModelMixin,
                     mixins.DestroyModelMixin,
                     GenericViewSet):
    queryset = Folder.objects.all()
    serializer_class = FoldersSerializer

    def get(self, request, *args, **kwargs):
        search_string = request.GET['search_string'] if 'search_string' in request.GET else ""
        if search_string:
            self.queryset = self.queryset.filter(name__icontains=search_string)
        return Response(FoldersSerializer(self.queryset, many=True))

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return Response(FoldersDetailSerializer(Folder.objects.get(pk=kwargs.get('pk'))).data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class DocumentsViewSet(mixins.ListModelMixin,
                       mixins.CreateModelMixin,
                       mixins.RetrieveModelMixin,
                       mixins.UpdateModelMixin,
                       mixins.DestroyModelMixin,
                       GenericViewSet):
    queryset = Document.objects.all()
    serializer_class = DocumentsSerializer

    def get(self, request, *args, **kwargs):
        folder = request.GET['folder'] if 'folder' in request.GET else ""
        topic = request.GET['topic'] if 'topic' in request.GET else ""
        self.queryset = self.queryset.filter(folder__id=folder)
        document_ids = self.queryset.values_list('id', flat=True)
        topic_association_documents = TopicAssociation.objects.filter(topic__id=topic,
                                                                      document__id__in=document_ids).\
            values_list('document', flat=True)
        return Response(DocumentsSerializer(set(topic_association_documents), many=True).data)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return Response(DocumentsDetailSerializer(Document.objects.get(pk=kwargs.get('pk'))).data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TopicsViewSet(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    GenericViewSet):
    queryset = Topic.objects.all()
    serializer_class = TopicsSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return Response(TopicsSerializer(Topic.objects.get(pk=kwargs.get('pk'))).data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class TopicAssociationViewSet(mixins.ListModelMixin,
                              mixins.CreateModelMixin,
                              mixins.RetrieveModelMixin,
                              mixins.UpdateModelMixin,
                              mixins.DestroyModelMixin,
                              GenericViewSet):
    queryset = TopicAssociation.objects.all()
    serializer_class = TopicAssociationSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        return Response(TopicsSerializer(Topic.objects.get(pk=kwargs.get('pk'))).data)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
