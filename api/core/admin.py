from django.contrib import admin
from .models import SteamPlatform, Watchlist, Review


@admin.register(SteamPlatform)
class SteamPlatformAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'price', 'genre', 'is_active')
    list_filter = ('is_active', 'genre')
    search_fields = ('title',)


@admin.register(Watchlist)
class WatchlistAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie_name', 'game', 'added_at')
    list_filter = ('movie_name', 'game')
    search_fields = ('movie_name', 'game__title')


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'watchlist', 'review', 'active', 'created')
    list_filter = ('active', 'review')
    search_fields = ('movie_name', 'watchlist__game__title')
