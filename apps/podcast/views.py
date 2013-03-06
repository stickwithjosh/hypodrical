from django import http
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.list_detail import object_list
from django.contrib.syndication.views import Feed
from models import Episode, Contributor, Podcast

# Create your views here.

def PodcastFeed(request):
    
    return object_list(
        request,
        mimetype='application/rss+xml',
        queryset=Episode.objects.order_by('-pub_date').filter(status=2)[0:21],
        template_name='podcast/feed.html')
        
class CanonicalDetailView(generic.DetailView):
    """
        A DetailView which redirects to the absolute_url, if necessary.
    """
    def get_object(self, *args, **kwargs):
        # Return any previously-cached object
        if getattr(self, 'object', None):
            return self.object
        return super(CanonicalDetailView, self).get_object(*args, **kwargs)

    def get(self, *args, **kwargs):
        # Make sure to use the canonical URL
        self.object = self.get_object()
        obj_url = self.object.get_absolute_url()
        if self.request.path != obj_url:
            return http.HttpResponsePermanentRedirect(obj_url)
        return super(CanonicalDetailView, self).get(*args, **kwargs);