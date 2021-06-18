import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Dict

from fastapi import APIRouter

from settings import COUNTS_RANGE
from utils import cpu_heavy, acpu_heavy

router = APIRouter()


@router.get('/count-sync')
async def count_sync() -> Dict[str, int]:
    res = [cpu_heavy(i) for i in range(COUNTS_RANGE)]
    return {'result': sum(res)}


@router.get('/count-threading')
async def count_threading() -> Dict[str, int]:
    with ThreadPoolExecutor() as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return {'result': sum(res)}


@router.get('/count-processing')
async def count_processing() -> Dict[str, int]:
    with ProcessPoolExecutor() as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return {'result': sum(res)}


@router.get('/count-async')
async def count_async() -> Dict[str, int]:
    return {'result': sum(await asyncio.gather(*[acpu_heavy(i) for i in range(COUNTS_RANGE)]))}
