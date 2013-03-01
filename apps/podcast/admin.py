from apps.podcast.models import Podcast, Contributor, Episode, Category
from django.contrib import admin

admin.site.register(Podcast)
admin.site.register(Contributor)

class EpisodeAdmin(admin.ModelAdmin):
    list_display = ('title', 'episode_number', 'pub_date')
    prepopulated_fields = {"slug": ("title",)}
    date_hierarchy = 'pub_date'
    
admin.site.register(Episode, EpisodeAdmin)