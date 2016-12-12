from __future__ import unicode_literals

from django.apps import AppConfig


class DiaryConfig(AppConfig):
    name = 'diary'


class DiaryRouter(object):
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'diary':
            return 'diary_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'diary':
            return 'diary_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'diary' or \
                                obj2._meta.app_label == 'diary':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'diary':
            return db == 'diary_db'
        return None
