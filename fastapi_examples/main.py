import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
from fastapi import FastAPI
import aiohttp
from fastapi.logger import logger


NUMBER_OF_REQUEST = 1000

URL_TO_BE_REQUESTED = 'http://127.0.0.1:8000/'

aio_logger = logger


app = FastAPI()


@app.get('/')
def home():
    return {'welcome_text': 'Welcome in FastAPI showcase project'}


@app.get('/fetch-sites-async')
async def fetch_sites_asyncio():
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(NUMBER_OF_REQUEST):
            task = asyncio.ensure_future(get_site(URL_TO_BE_REQUESTED, session))
            tasks.append(task)
        return await asyncio.gather(*tasks)


@app.get('/fetch-sites-threading')
def fetch_sites_threading():
    with ThreadPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUEST)))
    return res


@app.get('/fetch-sites-processing')
def fetch_sites_processing():
    with ProcessPoolExecutor() as ex:
        res = ex.map(get_response_body, (URL_TO_BE_REQUESTED for _ in range(NUMBER_OF_REQUEST)))
    return res


@app.get('/fetch-sites-sync')
def fetch_sites_sync():
    responses = []
    for i in range(NUMBER_OF_REQUEST):
        responses.append(requests.get(URL_TO_BE_REQUESTED).content)
    return responses


async def get_site(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        return await response.read()


def get_response_body(url):
    return requests.get(url).content