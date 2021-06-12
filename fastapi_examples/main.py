import uvicorn
from fastapi import FastAPI

from routers.api_requests import router as api_requests_router
from routers.math import router as math_router
from session_util import SingletonSession


def create_aiohttp_session():
    SingletonSession.get_session()


async def destroy_aiohttp_session():
    await SingletonSession.destroy_session()


app = FastAPI(docs_url='/docs', on_startup=[create_aiohttp_session], on_shutdown=[destroy_aiohttp_session])
app.include_router(api_requests_router)


@app.get('/')
def home():
    return {'welcome_text': 'Welcome to FastAPI showcase project'}

app.include_router(math_router)

if __name__ == '__main__':
    uvicorn.run('main:app', host="0.0.0.0", port=8080, reload=True)
