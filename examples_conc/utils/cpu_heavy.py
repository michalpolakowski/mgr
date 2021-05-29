import time
from typing import Tuple


def cpu_heavy(identification: int) -> Tuple[float, float]:
    print(f'Identification: {identification}')
    start = time.time()

    count = 0
    for i in range(10**8):
        count += i
    stop = time.time()

    print(f'Ended {identification} in {stop - start}')
    return start, stop
