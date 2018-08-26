from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    tag_name = models.CharField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.tag_name)


class Classification(models.Model):
    classification = models.CharField(max_length=100, blank=False)
    created_time = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return '%s' % (self.classification)


class PublicArticle(models.Model):
    article_title = models.CharField(max_length=100, blank=False)
    content = models.TextField(null=True)
    tags = models.ManyToManyField(Tag, null=True, blank=True)
    classification = models.ForeignKey(Classification, null=True)
    is_top = models.IntegerField(null=True)
    finalUrl = models.URLField(null=True)
    owner = models.ForeignKey(User, null=True)
    publish_time = models.DateTimeField(auto_now_add=False, null=True)
    save_time = models.DateTimeField(auto_now_add=False, null=True)
    is_published = models.BooleanField()
    is_draft = models.BooleanField()
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-is_top','-publish_time')




