import asyncio
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

from django.http import HttpResponse
from math_examples.utils import cpu_heavy, acpu_heavy

COUNTS_RANGE = 10000


def count_sync(_) -> HttpResponse:
    res = [cpu_heavy(i) for i in range(COUNTS_RANGE)]
    return HttpResponse({'result': sum(res)})


def count_threading(_) -> HttpResponse:
    with ThreadPoolExecutor() as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return HttpResponse({'result': sum(res)})


def count_processing(_) -> HttpResponse:
    with ProcessPoolExecutor() as ex:
        res = ex.map(cpu_heavy, range(COUNTS_RANGE))
    return HttpResponse(sum(res))


async def count_async(_) -> HttpResponse:
    return HttpResponse({'result': sum(await asyncio.gather(*[acpu_heavy(i) for i in range(COUNTS_RANGE)]))})
