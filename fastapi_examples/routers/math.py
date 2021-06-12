from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from typing import Dict, AsyncIterator

from fastapi import APIRouter

COUNTS_RANGE = 10000


def cpu_heavy(_: int) -> int:
    count = 0
    for i in range(1000):
        count += i
    return count


async def async_cpu_heavy(aiter: AsyncIterator):
    count = 0
    async for i in aiter:
        print(i)
        count += i
    return count


router = APIRouter()


@router.get('/count-sync')
async def count_sync() -> Dict[str, int]:
    x = 0
    for _ in range(COUNTS_RANGE):
        x += cpu_heavy(_)
    return {'result': x}


@router.get('/count-threading')
async def count_threading() -> Dict[str, int]:
    with ThreadPoolExecutor() as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return {'result': sum(res)}


@router.get('/count-processing')
async def count_processing() -> Dict[str, int]:
    with ProcessPoolExecutor(2) as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return {'result': sum(res)}
