# -*- coding: utf-8 -*-

from django.conf import settings


class BackendRouter(object):
    def __init__(self):
        self.applications_databases = settings.APPLICATIONS_DATABASES

    def db_for_read(self, model, **hints):
        app_label = model._meta.app_label
        database = self.applications_databases.get(app_label)
        return database

    def db_for_write(self, model, **hints):
        app_label = model._meta.app_label
        database = self.applications_databases.get(app_label)
        return database

    def allow_syncdb(self, db, model):
        databases = self.applications_databases.values()
        app_label = model._meta.app_label
        if db in databases:
            return db == self.applications_databases.get(app_label)
        else:
            return app_label not in self.applications_databases.keys()
