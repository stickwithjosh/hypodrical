from django.conf.urls import patterns, url 
from django.views.generic import ListView, DetailView
from django.views.generic.dates import *
from apps.podcast.models import Episode, Contributor
from apps.podcast.views import CanonicalDetailView, PodcastFeed
# Use Django's new date-based generic classes

urlpatterns = patterns('',
    url(r'^$', ArchiveIndexView.as_view(model=Episode, date_field="pub_date", queryset=Episode.objects.filter(status=2))),
    url(r'^contributors/$', ListView.as_view(
         queryset=Contributor.objects.select_related()
    )),
    url(r'^contributors/(?P<slug>[\w-]+)/*$', DetailView.as_view(model=Contributor), name='ContributorDetail'),
    url(r'feed/$', PodcastFeed,),
    url(r'^(?P<episode_number>\w+)/$', CanonicalDetailView.as_view(model=Episode)),
    url(r'^episode/(?P<slug>[\w-]+)/*$', DetailView.as_view(model=Episode), name='EpisodeDetail'),
    #url(r'^episode/(?P<slug>\w+)/$', DetailView.as_view(model=Episode)),
)

