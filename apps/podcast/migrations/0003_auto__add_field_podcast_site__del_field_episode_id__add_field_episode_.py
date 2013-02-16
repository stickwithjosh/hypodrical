# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Podcast.site'
        db.add_column('podcast_podcast', 'site',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='1', to=orm['sites.Site']),
                      keep_default=False)

        # Deleting field 'Episode.id'
        db.delete_column('podcast_episode', 'id')

        # Adding field 'Episode.episode_number'
        db.add_column('podcast_episode', 'episode_number',
                      self.gf('django.db.models.fields.AutoField')(default='1', primary_key=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Podcast.site'
        db.delete_column('podcast_podcast', 'site_id')

        # Adding field 'Episode.id'
        db.add_column('podcast_episode', 'id',
                      self.gf('django.db.models.fields.AutoField')(default='1', primary_key=True),
                      keep_default=False)

        # Deleting field 'Episode.episode_number'
        db.delete_column('podcast_episode', 'episode_number')


    models = {
        'podcast.category': {
            'Meta': {'object_name': 'Category'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'})
        },
        'podcast.contributor': {
            'Meta': {'object_name': 'Contributor'},
            'bio': ('django.db.models.fields.TextField', [], {}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            'home_url': ('django.db.models.fields.URLField', [], {'max_length': '200'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'twitter': ('django.db.models.fields.CharField', [], {'max_length': '150'})
        },
        'podcast.episode': {
            'Meta': {'object_name': 'Episode'},
            'artwork': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'contributors': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "'episodes'", 'blank': 'True', 'to': "orm['podcast.Contributor']"}),
            'episode_number': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('durationfield.db.models.fields.duration.DurationField', [], {'blank': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'show_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'podcast.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'artwork': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'categories': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['podcast.Category']", 'symmetrical': 'False'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['sites.Site']"}),
            'subtitle': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'summary': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['podcast']