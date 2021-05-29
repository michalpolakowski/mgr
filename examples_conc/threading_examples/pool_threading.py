from concurrent.futures import ThreadPoolExecutor
from typing import Callable


def pool_threading(function_to_be_triggered: Callable, length=10) -> list:
    with ThreadPoolExecutor() as ex:
        res = ex.map(function_to_be_triggered, range(length))
    return list(res)

