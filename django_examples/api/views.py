from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

URL_TO_BE_REQUESTED = 'http://localhost:8000/'
NUMBER_OF_REQUESTS = 1000


class HomeView(APIView):
    def get(self, _):
        return Response({'welcome': 'Welcome to django example project'})


@api_view()
def fetch_sites_threading(_):
    with ThreadPoolExecutor() as executor:
        res = executor.map(requests.get, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return Response(res)


@api_view()
def fetch_sites_processing(_):
    with ProcessPoolExecutor() as executor:
        res = executor.map(requests.get, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return Response(res)
