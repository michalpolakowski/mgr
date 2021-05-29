from concurrent.futures import ProcessPoolExecutor
from typing import Callable


def pool_processing(function_to_be_triggered: Callable, length=10) -> list:
    with ProcessPoolExecutor() as ex:
        res = ex.map(function_to_be_triggered, range(length))
    return list(res)
