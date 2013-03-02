# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Category'
        db.create_table('podcast_category', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
        ))
        db.send_create_signal('podcast', ['Category'])

        # Adding model 'Podcast'
        db.create_table('podcast_podcast', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('subtitle', self.gf('django.db.models.fields.CharField')(max_length=300, blank=True)),
            ('summary', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('keywords', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('artwork', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('author', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('author_email', self.gf('django.db.models.fields.EmailField')(max_length=75, blank=True)),
            ('copyright', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('site', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['sites.Site'])),
        ))
        db.send_create_signal('podcast', ['Podcast'])

        # Adding M2M table for field categories on 'Podcast'
        db.create_table('podcast_podcast_categories', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('podcast', models.ForeignKey(orm['podcast.podcast'], null=False)),
            ('category', models.ForeignKey(orm['podcast.category'], null=False))
        ))
        db.create_unique('podcast_podcast_categories', ['podcast_id', 'category_id'])

        # Adding model 'Contributor'
        db.create_table('podcast_contributor', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=300)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('twitter', self.gf('django.db.models.fields.CharField')(max_length=150)),
            ('home_url', self.gf('django.db.models.fields.URLField')(max_length=200)),
            ('bio', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('podcast', ['Contributor'])

        # Adding model 'Episode'
        db.create_table('podcast_episode', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('slug', self.gf('django.db.models.fields.SlugField')(max_length=50, blank=True)),
            ('episode_number', self.gf('django.db.models.fields.IntegerField')(unique=True)),
            ('pub_date', self.gf('django.db.models.fields.DateTimeField')(blank=True)),
            ('length', self.gf('durationfield.db.models.fields.duration.DurationField')(blank=True)),
            ('show_notes', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('artwork', self.gf('django.db.models.fields.files.ImageField')(max_length=100, blank=True)),
            ('mp3', self.gf('django.db.models.fields.files.FileField')(max_length=100, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('podcast', ['Episode'])

        # Adding M2M table for field contributors on 'Episode'
        db.create_table('podcast_episode_contributors', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('episode', models.ForeignKey(orm['podcast.episode'], null=False)),
            ('contributor', models.ForeignKey(orm['podcast.contributor'], null=False))
        ))
        db.create_unique('podcast_episode_contributors', ['episode_id', 'contributor_id'])


    def backwards(self, orm):
        # Deleting model 'Category'
        db.delete_table('podcast_category')

        # Deleting model 'Podcast'
        db.delete_table('podcast_podcast')

        # Removing M2M table for field categories on 'Podcast'
        db.delete_table('podcast_podcast_categories')

        # Deleting model 'Contributor'
        db.delete_table('podcast_contributor')

        # Deleting model 'Episode'
        db.delete_table('podcast_episode')

        # Removing M2M table for field contributors on 'Episode'
        db.delete_table('podcast_episode_contributors')


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
            'episode_number': ('django.db.models.fields.IntegerField', [], {'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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