from django.db import models
import tagging
from durationfield.db.models.fields.duration import DurationField
from django.contrib.sites.models import Site


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
            return u'%s - %s' % (self.episode, self.name)


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


class Episode(models.Model):
    title = models.CharField(max_length=500, blank=True)
    slug = models.SlugField(blank=True, )
    episode_number = models.IntegerField(unique=True, blank=True)
    contributors = models.ManyToManyField('Contributor', blank=True, related_name='episodes')
    pub_date = models.DateTimeField('date published', blank=True)
    length = DurationField(blank=True, )
    short_description = models.TextField(blank=True, ),
    show_notes = models.TextField(blank=True)
    artwork = models.ImageField(blank=True, upload_to='e/art')
    mp3 = models.FileField(blank=True, upload_to='e')
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

tagging.register(Episode)
