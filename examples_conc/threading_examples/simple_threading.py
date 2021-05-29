from threading import Thread
from typing import Callable


def simple_threading(function_to_be_triggered: Callable, length=10) -> None:
    processes = []
    for i in range(length):
        processes.append(Thread(target=function_to_be_triggered, args=(i,)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
