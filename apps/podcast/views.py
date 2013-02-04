from django.views.generic import TemplateView
from django.views.generic.list_detail import object_list
from django.contrib.syndication.views import Feed
from models import Episode, Contributor, Podcast

# Create your views here.

def podcast_feed(request):

    return object_list(
        request,
        mimetype='application/rss+xml',
        queryset=Episode.objects.order_by('-pub_date')[0:21],
        template_name='podcast/feed.html')
                                                  