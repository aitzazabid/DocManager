from django.db import models


class Folder(models.Model):
    name = models.CharField(max_length=1024)


class Document(models.Model):
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE)
    name = models.CharField(max_length=1024)


class Topic(models.Model):
    name = models.CharField(max_length=1024)
    short_description = models.TextField(default='', null=True, blank=True)
    long_description = models.TextField(default='', null=True, blank=True)


class TopicAssociation(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    folder = models.ForeignKey(Folder, on_delete=models.CASCADE, null=True)
    document = models.ForeignKey(Document, on_delete=models.CASCADE, null=True)
