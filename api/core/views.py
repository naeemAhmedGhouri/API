from rest_framework.viewsets import ModelViewSet
from .models import SteamPlatform, Watchlist, Review
from .serializers import SteamPlatformSerializer, WatchlistSerializer, ReviewSerializer
from rest_framework import generics
from .models import Review

class SteamPlatformViewSet(ModelViewSet):
    queryset = SteamPlatform.objects.all()
    serializer_class = SteamPlatformSerializer



class WatchlistViewSet(ModelViewSet):
    queryset = Watchlist.objects.all()
    serializer_class = WatchlistSerializer


class ReviewCreate(generics.CreateAPIView):
    serializer_class = ReviewSerializer

    def perform_create(self, serializer):
        pk = self.kwargs['pk']
        watchlist = Watchlist.objects.get(pk=pk)
        serializer.save(watchlist=watchlist)

class ReviewListView(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Review.objects.filter(watchlist = pk)


class ReviewDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer