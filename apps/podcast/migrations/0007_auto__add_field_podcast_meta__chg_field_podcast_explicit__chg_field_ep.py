# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Podcast.meta'
        db.add_column('podcast_podcast', 'meta',
                      self.gf('django.db.models.fields.TextField')(default='', blank=True),
                      keep_default=False)


        # Changing field 'Podcast.explicit'
        db.alter_column('podcast_podcast', 'explicit', self.gf('django.db.models.fields.CharField')(max_length=3))

        # Changing field 'Episode.explicit'
        db.alter_column('podcast_episode', 'explicit', self.gf('django.db.models.fields.CharField')(max_length=3))

    def backwards(self, orm):
        # Deleting field 'Podcast.meta'
        db.delete_column('podcast_podcast', 'meta')


        # Changing field 'Podcast.explicit'
        db.alter_column('podcast_podcast', 'explicit', self.gf('django.db.models.fields.CharField')(max_length=1))

        # Changing field 'Episode.explicit'
        db.alter_column('podcast_episode', 'explicit', self.gf('django.db.models.fields.CharField')(max_length=1))

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
            'episode_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True', 'blank': 'True'}),
            'explicit': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'length': ('durationfield.db.models.fields.duration.DurationField', [], {'blank': 'True'}),
            'mp3': ('django.db.models.fields.files.FileField', [], {'max_length': '100', 'blank': 'True'}),
            'pub_date': ('django.db.models.fields.DateTimeField', [], {'blank': 'True'}),
            'show_notes': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'})
        },
        'podcast.podcast': {
            'Meta': {'object_name': 'Podcast'},
            'artwork': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'}),
            'author': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'author_email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'copyright': ('django.db.models.fields.CharField', [], {'max_length': '300'}),
            'explicit': ('django.db.models.fields.CharField', [], {'default': "'1'", 'max_length': '3', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'keywords': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'meta': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '300', 'blank': 'True'}),
            'site': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'podcasts'", 'to': "orm['sites.Site']"}),
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