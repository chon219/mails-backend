# -*- coding: utf-8 -*-

from django.db import models


class Application(models.Model):
    name = models.CharField(max_length=64)
    host = models.CharField(max_length=128)
    port = models.IntegerField(default=25)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)
    use_ssl = models.BooleanField(default=False)
    default_sender = models.CharField(max_length=128)

    def __unicode__(self):
        return unicode(self.name)

    class Meta:
        db_table = 'application'


class Log(models.Model):
    application = models.ForeignKey(Application)
    sender = models.CharField(max_length=128)
    receiver = models.CharField(max_length=128)
    subject = models.CharField(max_length=256)
    content = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return unicode(self.subject)

    class Meta:
        db_table = 'log'


class Template(models.Model):
    application = models.ForeignKey(Application)
    name = models.CharField(max_length=64)
    subject = models.CharField(max_length=256)
    content = models.TextField()

    def __unicode__(self):
        return unicode(self.subject)

    class Meta:
        db_table = 'template'
