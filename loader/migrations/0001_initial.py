# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'StateEquiv'
        db.create_table('loader_stateequiv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal('loader', ['StateEquiv'])

        # Adding model 'CountyEquiv'
        db.create_table('loader_countyequiv', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('code', self.gf('django.db.models.fields.CharField')(max_length=5, unique=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loader.StateEquiv'])),
        ))
        db.send_create_signal('loader', ['CountyEquiv'])

        # Adding model 'CountyArchive'
        db.create_table('loader_countyarchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('extent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loader.CountyEquiv'])),
        ))
        db.send_create_signal('loader', ['CountyArchive'])

        # Adding model 'StateArchive'
        db.create_table('loader_statearchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=11)),
            ('extent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['loader.StateEquiv'])),
        ))
        db.send_create_signal('loader', ['StateArchive'])

        # Adding model 'NationalArchive'
        db.create_table('loader_nationalarchive', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=8)),
        ))
        db.send_create_signal('loader', ['NationalArchive'])


    def backwards(self, orm):
        # Deleting model 'StateEquiv'
        db.delete_table('loader_stateequiv')

        # Deleting model 'CountyEquiv'
        db.delete_table('loader_countyequiv')

        # Deleting model 'CountyArchive'
        db.delete_table('loader_countyarchive')

        # Deleting model 'StateArchive'
        db.delete_table('loader_statearchive')

        # Deleting model 'NationalArchive'
        db.delete_table('loader_nationalarchive')


    models = {
        'loader.countyarchive': {
            'Meta': {'object_name': 'CountyArchive'},
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.CountyEquiv']"}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'loader.countyequiv': {
            'Meta': {'object_name': 'CountyEquiv'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.StateEquiv']"})
        },
        'loader.nationalarchive': {
            'Meta': {'object_name': 'NationalArchive'},
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '8'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'loader.statearchive': {
            'Meta': {'object_name': 'StateArchive'},
            'extent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['loader.StateEquiv']"}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '11'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'loader.stateequiv': {
            'Meta': {'object_name': 'StateEquiv'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['loader']