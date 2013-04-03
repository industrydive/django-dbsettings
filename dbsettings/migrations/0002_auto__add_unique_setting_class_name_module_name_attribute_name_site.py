# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Setting', fields ['class_name', 'module_name', 'attribute_name', 'site']
        db.create_unique('dbsettings_setting', ['class_name', 'module_name', 'attribute_name', 'site_id'])


    def backwards(self, orm):
        # Removing unique constraint on 'Setting', fields ['class_name', 'module_name', 'attribute_name', 'site']
        db.delete_unique('dbsettings_setting', ['class_name', 'module_name', 'attribute_name', 'site_id'])


    models = {
        'dbsettings.setting': {
            'Meta': {'unique_together': "(('site', 'module_name', 'class_name', 'attribute_name'),)", 'object_name': 'Setting'},
            'attribute_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'class_name': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'module_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['dbsettings']