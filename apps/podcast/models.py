import os
import tagging

from django.db import models
from django.contrib.sites.models import Site
from django.conf import settings
from django.template.defaultfilters import slugify

from durationfield.db.models.fields.duration import DurationField

from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC, error


EPISODE_STATUS = (
    ('1', 'Draft'),
    ('2', 'Public'),
)

EXPLICITNESS = (
    ('yes', 'Dirty'),
    ('no', 'Clean'),
)


class Category(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
            return u'%s' % self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Podcast(models.Model):
    name = models.CharField(max_length=300, help_text='The name of the podcast')
    subtitle = models.CharField(max_length=300, blank=True,
                                help_text='One line descriptor')
    summary = models.TextField(blank=True,
                               help_text='Paragraph or more description')
    keywords = models.TextField(blank=True, help_text='iTunes Categories')
    artwork = models.ImageField(blank=True, upload_to='podcastart/%Y/%m/%d',
                                help_text='Cover art for the podcast, iTunes prefers 1400x1400 because it ends up on TVs and retina screens and whatnot')
    author = models.CharField(max_length=300, blank=True,
                              help_text='This shows up underneath the title in iTunes, I like to use the hosts\' names')
    author_email = models.EmailField(blank=True,
                                     help_text='Should be a string similar to x@y.coms')
    copyright = models.CharField(max_length=300)
    site = models.ForeignKey(Site, related_name='podcasts')
    explicit = models.CharField(max_length=3, choices=EXPLICITNESS,
                                blank=True, default='1', help_text='Is the podcast dirrrty?')
    meta = models.TextField(help_text="for the base.html file, markdown formatted HTMLz", blank=True)
    ga_code = models.CharField(max_length=200, blank=True)

    def __unicode__(self):
            return u'%s' % self.name


class Contributor(models.Model):
    name = models.CharField(max_length=300)
    slug = models.SlugField(blank=True)
    email = models.EmailField()
    twitter = models.CharField(max_length=150)
    home_url = models.URLField()
    bio = models.TextField()

    def __unicode__(self):
            return u'%s' % self.name

    @models.permalink
    def get_absolute_url(self):
        return ('ContributorDetail', (), {'slug': str(self.slug)})


def rename_uploaded_file(instance, filename):
    #TODO: figure out how to get podcast name in there
    return os.path.join('e', "%s_%s.mp3" % (instance.episode_number, slugify(instance.title)))


class Episode(models.Model):
    title = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(blank=True, )
    podcast = models.ForeignKey(Podcast)
    episode_number = models.IntegerField(unique=True, blank=True)
    contributors = models.ManyToManyField('Contributor', blank=True, related_name='episodes')
    pub_date = models.DateTimeField('date published', blank=True)
    length = DurationField(blank=True, )
    short_description = models.TextField(blank=True, ),
    show_notes = models.TextField(blank=True)
    artwork = models.ImageField(blank=True, upload_to='e/art')
    mp3 = models.FileField(blank=True, upload_to=rename_uploaded_file)
    status = models.CharField(max_length=1, choices=EPISODE_STATUS, blank=True)
    explicit = models.CharField(max_length=3, choices=EXPLICITNESS, blank=True,
                                default='1',
                                help_text='Dirt McGirt (did you cut the badwords?)')

    def __unicode__(self):
            return u'%s %s' % (self.episode_number, self.title)

    @models.permalink
    def get_absolute_url(self):
        return ('EpisodeDetail', (), {'slug': str(self.slug)})

    class Meta:
        ordering = ['-pub_date']

    def save(self, *args, **kwargs):

        super(Episode, self).save(*args, **kwargs)

        if self.artwork or self.podcast.artwork:
            # Look for episode artwork first
            if self.artwork:
                artwork = self.artwork.read()
            # if not then use the podcast artwork
            elif self.podcast.artwork:
                artwork = self.podcast.artwork.read()

            mp3 = settings.APP_DIR + self.mp3.url
            audio = MP3(mp3, ID3=ID3)

            # add ID3 tag if it doesn't exist
            try:
                audio.add_tags()
            except error:
                pass

            audio.tags.add(
                APIC(
                    encoding=3,  # 3 is for utf-8
                    mime='image/png',  # image/jpeg or image/png
                    type=3,  # 3 is for the cover image
                    desc=u'Cover',
                    data=artwork
                )
            )
            audio.save()

            super(Episode, self).save(*args, **kwargs)

tagging.register(Episode)
