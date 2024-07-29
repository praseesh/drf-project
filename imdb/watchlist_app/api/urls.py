from django.urls import include, path
from watchlist_app.api import views
from rest_framework.routers import DefaultRouter
from .views import StreamPlatformVS

router = DefaultRouter()
router.register(r'stream', StreamPlatformVS, basename='streamplatform')

urlpatterns = [

    path('list/', views.WatchListAV.as_view(), name="movie-list" ),
    path('<int:pk>/',views.WatchDetailAV.as_view(), name='movie_detail'),
    path('', include(router.urls)),
    # path('stream/', views.StreamPlatformAV.as_view(), name="streamplatform-list"),
    # path('stream/<int:pk>/', views.StreamDetailAV.as_view(), name="streamplatform-detail" ),

    path('stream/<int:pk>/review-create/', views.ReviewCreate.as_view(), name="review-create" ),
    path('stream/<int:pk>/review/', views.ReviewList.as_view(), name="review-list" ),
    path('stream/review/<int:pk>/', views.ReviewDetail.as_view(), name="review-detail"),
        
    # path('review/', views.ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>/', views.ReviewDetail.as_view(), name="review-detail"),
]
