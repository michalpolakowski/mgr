import time
from typing import List


def do_nothing_and_gather_times(identification: int) -> List[float]:
    print(f'Indentification: {identification}')
    start = time.time()
    res = []
    for i in range(10**6):
        res.append(time.time() - start)
    return res

async def ado_nothing_and_gather_times(identification: int) -> List[float]:
    print(f'Indentification: {identification}')
    start = time.time()
    res = []
    for i in range(10**6):
        res.append(time.time() - start)
    return res
