from django.urls import path
from watchlist_app.api import views

urlpatterns = [

    path('list/', views.WatchListAV.as_view(), name="movie-list" ),
    path('<int:pk>/',views.WatchDetailAV.as_view(), name='movie_detail'),
    path('stream/', views.StreamPlatformAV.as_view(), name="streamplatform-list"),
    path('stream/<int:pk>/', views.StreamDetailAV.as_view(), name="streamplatform-detail" )
]
