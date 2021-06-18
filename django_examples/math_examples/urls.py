from django.urls import path

from math_examples.views import count_sync, count_threading, count_processing, count_async

urlpatterns = [
    path('count-sync', count_sync),
    path('count-threading', count_threading),
    path('count-processing', count_processing),
    path('count-async', count_async)
]
