from django.conf.urls import patterns, include, url
from django.contrib import admin


from apps.podcast.models import Episode

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('apps.podcast.urls')),
)
