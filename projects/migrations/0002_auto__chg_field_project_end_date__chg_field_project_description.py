# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Project.end_date'
        db.alter_column(u'projects_project', 'end_date', self.gf('django.db.models.fields.DateField')(null=True))

        # Changing field 'Project.description'
        db.alter_column(u'projects_project', 'description', self.gf('django.db.models.fields.TextField')(null=True))

    def backwards(self, orm):

        # User chose to not deal with backwards NULL issues for 'Project.end_date'
        raise RuntimeError("Cannot reverse this migration. 'Project.end_date' and its values cannot be restored.")

        # User chose to not deal with backwards NULL issues for 'Project.description'
        raise RuntimeError("Cannot reverse this migration. 'Project.description' and its values cannot be restored.")

    models = {
        u'projects.project': {
            'Meta': {'object_name': 'Project'},
            'description': ('django.db.models.fields.TextField', [], {'null': 'True'}),
            'end_date': ('django.db.models.fields.DateField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'progress': ('django.db.models.fields.PositiveSmallIntegerField', [], {'default': '0'}),
            'start_date': ('django.db.models.fields.DateField', [], {}),
            'technologies': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['projects.Technology']", 'symmetrical': 'False'})
        },
        u'projects.technology': {
            'Meta': {'object_name': 'Technology'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['projects']