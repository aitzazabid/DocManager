from rest_framework import serializers
from doc_manager_app.models import Folder, Document, Topic, TopicAssociation


class FoldersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Folder
        fields = '__all__'


class FoldersDetailSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField("get_topics")
    documents = serializers.SerializerMethodField("get_documents")

    def get_topics(self, obj):
        topic_ids = TopicAssociation.objects.filter(folder=obj).values_list('topic_id', flat=Topic)
        topics = Topic.objects.filter(id__in=topic_ids)
        return TopicsSerializer(topics, many=True).data

    def get_documents(self, obj):
        return DocumentsSerializer(obj.document_set.all(), many=True).data
    class Meta:
        model = Folder
        fields = '__all__'


class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'


class DocumentsDetailSerializer(serializers.ModelSerializer):
    topics = serializers.SerializerMethodField("get_topics")

    def get_topics(self, obj):
        topic_ids = TopicAssociation.objects.filter(document=obj).values_list('topic_id', flat=Topic)
        topics = Topic.objects.filter(id__in=topic_ids)
        return TopicsSerializer(topics, many=True).data

    class Meta:
        model = Document
        fields = '__all__'


class TopicsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = '__all__'


class TopicAssociationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TopicAssociation
        fields = '__all__'
