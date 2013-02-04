from django.conf.urls import patterns, url 
from django.views.generic import ListView, DetailView
from django.views.generic.dates import *
from apps.podcast.models import Episode

# Use Django's new date-based generic classes

urlpatterns = patterns('',
    # url(r'^(?P\d{4})/(?P\d{2})/$',
    #     MonthArchiveView.as_view(
    #         model=Episode,
    #         date_field='pub_date',
    #     )   
    # ),  
    # url(r'^(?P\d{4})/$',
    #     YearArchiveView.as_view(
    #         model=Episode,
    #         make_object_list=True,
    #         date_field='pub_date',
    #     )   
    # ),  
    # url(r'^', ListView.as_view(
    #     queryset=Episode.objects.select_related()
    # )), 
    url(r'^(?P<slug>\w+)/$', DetailView.as_view(model=Episode, slug_field='slug')),
    url(r'^mydetail/(?P<pk>\w+)/$', DetailView.as_view(model=Episode))
)

