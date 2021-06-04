from django.urls import path

from api.views import fetch_sites_threading, HomeView

urlpatterns = [
    path('', HomeView.as_view()),
    path('fetch-sites-threading', fetch_sites_threading)
]