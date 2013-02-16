from apps.podcast.models import Podcast, Contributor, Episode, Category
from django.contrib import admin

admin.site.register(Podcast)
admin.site.register(Contributor)
admin.site.register(Episode)
class EpisodeAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
admin.site.register(Category)