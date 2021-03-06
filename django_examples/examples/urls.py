from django.urls import path

from examples.views import fetch_sites_threading, fetch_sites_processing, fetch_sites_async, welcome_page, \
    fetch_sites_sync

urlpatterns = [
    path('', welcome_page),
    path('fetch-sites-sync', fetch_sites_sync),
    path('fetch-sites-threading', fetch_sites_threading),
    path('fetch-sites-processing', fetch_sites_processing),
    path('fetch-sites-async', fetch_sites_async)
]
