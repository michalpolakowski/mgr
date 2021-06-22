from threading import Thread
from typing import Callable


def simple_threading(function_to_be_triggered: Callable, length=10) -> None:
    threads = []
    for i in range(length):
        threads.append(Thread(target=function_to_be_triggered, args=(i,)))
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
