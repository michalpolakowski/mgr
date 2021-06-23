import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
from django.http import JsonResponse

from examples import session


URL_TO_BE_REQUESTED = 'http://localhost:8000/'
NUMBER_OF_REQUESTS = 1000


def welcome_page(_):
    return JsonResponse({'welcome': 'Welcome to django example project'})


def fetch_sites_sync(_):
    responses = []
    for i in range(NUMBER_OF_REQUESTS):
        responses.append(get_response_body(URL_TO_BE_REQUESTED))
    return JsonResponse(responses, safe=False)


def fetch_sites_threading(_):
    with ThreadPoolExecutor() as executor:
        res = executor.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return JsonResponse([welcome_text for welcome_text in res], safe=False)


def fetch_sites_processing(_):
    with ProcessPoolExecutor() as executor:
        res = executor.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return JsonResponse([welcome_text for welcome_text in res], safe=False)


async def fetch_sites_async(_):
    tasks = []
    for i in range(NUMBER_OF_REQUESTS):
        tasks.append(get_site(URL_TO_BE_REQUESTED))
    res = await asyncio.gather(*tasks)
    return JsonResponse([welcome_text for welcome_text in res], safe=False)


async def get_site(url: str):
    async with session.AIOHTTP_CLIENT_SESSION.get(url) as response:
        return await response.json()


def get_response_body(url):
    return requests.get(url).json()
