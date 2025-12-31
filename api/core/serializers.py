from rest_framework import serializers
from .models import SteamPlatform, Watchlist, Review
from django.contrib.auth.models import User


class SteamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = SteamPlatform
        fields = '__all__'


class WatchlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = '__all__'
class ReviewSerializer(serializers.ModelSerializer):
    Reviewuser = serializers.StringRelatedField(source='watchlist.user', read_only=True)
    class Meta:
        model = Review
        fields='__all__'