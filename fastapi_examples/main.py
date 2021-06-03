import asyncio

from fastapi import FastAPI
import aiohttp

app = FastAPI()


@app.get('/')
def home():
    return {'welcome_text': 'Welcome in FastAPI showcase project'}


@app.get('/fetch-sites')
async def fetch_sites():
    url = "https://www.google.com"
    tasks = []
    async with aiohttp.ClientSession() as session:
        for i in range(8):
            task = asyncio.ensure_future(get_site(url, session))
            tasks.append(task)
        responses = await asyncio.gather(*tasks)
        return responses


async def get_site(url: str, session: aiohttp.ClientSession):
    async with session.get(url) as response:
        return await response.read()
