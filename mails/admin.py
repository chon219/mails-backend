# -*- coding: utf-8 -*-

from django.contrib import admin


from mails.models import Application
from mails.models import Log
from mails.models import Template


class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'username', 'default_sender',)


class LogAdmin(admin.ModelAdmin):
    list_display = ('application', 'receiver', 'subject', 'datetime',)
    list_filter = ('application',)


class TemplateAdmin(admin.ModelAdmin):
    list_display = ('application', 'name', 'subject',)
    list_filter = ('application',)


admin.site.register(Application, ApplicationAdmin)
admin.site.register(Log, LogAdmin)
admin.site.register(Template, TemplateAdmin)
