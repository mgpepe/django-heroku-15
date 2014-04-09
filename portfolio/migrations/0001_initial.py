# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Client'
        db.create_table(u'portfolio_client', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('contact_person', self.gf('django.db.models.fields.CharField')(max_length=200)),
        ))
        db.send_create_signal(u'portfolio', ['Client'])

        # Adding model 'Project'
        db.create_table(u'portfolio_project', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('text', self.gf('django.db.models.fields.TextField')()),
            ('link', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('link_display', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('default_large', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_large', null=True, to=orm['portfolio.Image'])),
            ('default_medium', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_medium', null=True, to=orm['portfolio.Image'])),
            ('default_small', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='default_small', null=True, to=orm['portfolio.Image'])),
            ('client', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Client'])),
            ('use_in', self.gf('django.db.models.fields.IntegerField')(default=2)),
            ('what_we_did', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'portfolio', ['Project'])

        # Adding model 'Image'
        db.create_table(u'portfolio_image', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('file', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('project', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['portfolio.Project'])),
            ('size', self.gf('django.db.models.fields.CharField')(max_length=100)),
        ))
        db.send_create_signal(u'portfolio', ['Image'])


    def backwards(self, orm):
        # Deleting model 'Client'
        db.delete_table(u'portfolio_client')

        # Deleting model 'Project'
        db.delete_table(u'portfolio_project')

        # Deleting model 'Image'
        db.delete_table(u'portfolio_image')


    models = {
        u'portfolio.client': {
            'Meta': {'object_name': 'Client'},
            'contact_person': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portfolio.image': {
            'Meta': {'object_name': 'Image'},
            'file': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Project']"}),
            'size': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        u'portfolio.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['portfolio.Client']"}),
            'default_large': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_large'", 'null': 'True', 'to': u"orm['portfolio.Image']"}),
            'default_medium': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_medium'", 'null': 'True', 'to': u"orm['portfolio.Image']"}),
            'default_small': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'default_small'", 'null': 'True', 'to': u"orm['portfolio.Image']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'link': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'link_display': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'text': ('django.db.models.fields.TextField', [], {}),
            'use_in': ('django.db.models.fields.IntegerField', [], {'default': '2'}),
            'what_we_did': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['portfolio']