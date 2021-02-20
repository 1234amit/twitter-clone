from django.urls import path
from tweets import views

app_name = 'tweets'

urlpatterns = [
    path('', views.home_view, name="home"),
    path('tweets/', views.tweet_list_view, name="tweets"),
]