# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'CountyArchive.size'
        db.add_column('loader_countyarchive', 'size',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'StateArchive.size'
        db.add_column('loader_statearchive', 'size',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)

        # Adding field 'NationalArchive.size'
        db.add_column('loader_nationalarchive', 'size',
                      self.gf('django.db.models.fields.BigIntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'CountyArchive.size'
        db.delete_column('loader_countyarchive', 'size')

        # Deleting field 'StateArchive.size'
        db.delete_column('loader_statearchive', 'size')

        # Deleting field 'NationalArchive.size'
        db.delete_column('loader_nationalarchive', 'size')


    models = {
        'loader.countyarchive': {
            'Meta': {'object_name': 'CountyArchive'},
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.CountyEquiv']"}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'loader.countyequiv': {
            'Meta': {'object_name': 'CountyEquiv'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.StateEquiv']"})
        },
        'loader.nationalarchive': {
            'Meta': {'object_name': 'NationalArchive'},
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'loader.statearchive': {
            'Meta': {'object_name': 'StateArchive'},
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.StateEquiv']"}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'size': ('django.db.models.fields.BigIntegerField', [], {})
        },
        'loader.stateequiv': {
            'Meta': {'object_name': 'StateEquiv'},
            'code': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['loader']