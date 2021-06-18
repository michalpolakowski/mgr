import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
from django.http import HttpResponse, JsonResponse

from examples import session


URL_TO_BE_REQUESTED = 'http://localhost:8000/'
NUMBER_OF_REQUESTS = 100


def welcome_page(_):
    return JsonResponse({'welcome': 'Welcome to django example project'})


def fetch_sites_sync(_):
    responses = []
    for i in range(NUMBER_OF_REQUESTS):
        responses.append(get_response_body(URL_TO_BE_REQUESTED))
    return HttpResponse(responses)


def fetch_sites_threading(_):
    with ThreadPoolExecutor() as executor:
        res = executor.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return HttpResponse(res)


def fetch_sites_processing(_):
    with ProcessPoolExecutor() as executor:
        res = executor.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUESTS)))
    return HttpResponse(res)


async def fetch_sites_async(_):
    tasks = []
    for i in range(NUMBER_OF_REQUESTS):
        tasks.append(get_site(URL_TO_BE_REQUESTED))
    res = await asyncio.gather(*tasks)
    return HttpResponse(res)


async def get_site(url: str):
    print(session.AIOHTTP_CLIENT_SESSION)
    async with session.AIOHTTP_CLIENT_SESSION.get(url) as response:
        return await response.read()


def get_response_body(url):
    return requests.get(url).content