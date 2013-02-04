from django.db import models
import tagging
from durationfield.db.models.fields.duration import DurationField

EPISODE_STATUS = (
    ('1', 'Draft'),
    ('2', 'Public'),
)

class Category(models.Model):
    name = models.CharField(max_length=300)

    def __unicode__(self):
            return u'%s' % self.name
            
    class Meta:
        verbose_name_plural = 'Categories'
    
class Podcast(models.Model):
    name = models.CharField(max_length=300,blank=True, )
    subtitle = models.CharField(max_length=300,blank=True, )
    summary = models.TextField(blank=True, )
    keywords = models.TextField(blank=True, )
    artwork = models.ImageField(blank=True, upload_to='podcastart/%Y/%m/%d')
    author = models.CharField(max_length=300)
    author_email = models.EmailField(blank=True, )
    copyright = models.CharField(max_length=300)
    categories = models.ManyToManyField(Category)
    
    def __unicode__(self):
            return u'%s' % self.name
    
    
class Contributor(models.Model):
    name = models.CharField(max_length=300)
    twitter = models.CharField(max_length=150)
    home_url = models.URLField()
    bio = models.TextField()
    
    def __unicode__(self):
            return u'%s' % self.name
    
    
class Episode(models.Model):
    title = models.CharField(max_length=500,blank=True, )
    slug = models.SlugField(blank=True, )
    contributors = models.ManyToManyField('Contributor', blank=True, )
    pub_date = models.DateTimeField('date published',blank=True, )
    length = DurationField(blank=True, )
    show_notes = models.TextField(blank=True)
    artwork = models.ImageField(blank=True, upload_to='episodeart/%Y/%m/%d')
    mp3 = models.FileField(blank=True, upload_to='e/slug')
    status = models.CharField(max_length=1, choices=EPISODE_STATUS)
    
    def __unicode__(self):
            return u'%s' % self.title
    
tagging.register(Episode)