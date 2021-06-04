import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import requests
import uvicorn
from fastapi import FastAPI
import aiohttp

from session_util import SingletonSession

PORT = 8080
NUMBER_OF_REQUEST = 1000
URL_TO_BE_REQUESTED = f'http://localhost:{PORT}/'


def create_aiohttp_session():
    SingletonSession.get_session()


async def destroy_aiohttp_session():
    await SingletonSession.destroy_session()


app = FastAPI(docs_url='/docs', on_startup=[create_aiohttp_session], on_shutdown=[destroy_aiohttp_session])


@app.get('/')
def home():
    return {'welcome_text': 'Welcome in FastAPI showcase project'}


@app.get('/fetch-sites-async')
async def fetch_sites_asyncio():
    tasks = []
    for i in range(NUMBER_OF_REQUEST):
        tasks.append(SingletonSession.fetch_url(URL_TO_BE_REQUESTED))
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


if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=PORT, reload=True)
