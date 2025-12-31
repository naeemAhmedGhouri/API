
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SteamPlatformViewSet, WatchlistViewSet
from .views import ReviewListView, ReviewDetailView, ReviewCreate
# from api.core.views import api_root

api_root = lambda request: None  # Placeholder for api_root view
router = DefaultRouter()
router.register(r'steam-platforms', SteamPlatformViewSet)
router.register(r'watchlists', WatchlistViewSet)
# router.register(r'reviews', ReviewListView.as_view(), basename='review')
urlpatterns = router.urls + [
    path('', include(router.urls)),
    path('list/<int:pk>/review', ReviewListView.as_view(), name='review-list'),
    path('list/<int:pk>/review-create', ReviewCreate.as_view(), name='review-create'),
    path('list/review/<int:pk>/', ReviewDetailView.as_view(), name='review-detail'),
    path('', include(router.urls)),
    path("", api_root),
    ]
 