import datetime

from django.views.generic.list_detail import object_list
from django.shortcuts import get_object_or_404, redirect
from models import Episode


def PodcastFeed(request):
    """ Fetch the most recent 21? episodes
        showing most recent first and excluding
        episodes that are set to publish in the future

    """
    queryset = Episode.objects.filter(status=2,
        pub_date__lte=datetime.datetime.now()).order_by('-pub_date')[:21]

    return object_list(
        request,
        mimetype='application/rss+xml',
        queryset=queryset,
        template_name='podcast/feed.html')


def canonical_redirect(request, episode_number):
    """ Look for the episode number passed
        and redirect to the right url
        otherwise render a 404

    """

    episode = get_object_or_404(Episode, episode_number=episode_number)
    return redirect(episode)
