from multiprocessing import Process
from typing import Callable


def simple_processing(function_to_be_triggered: Callable, length=10) -> None:
    processes = []
    for i in range(length):
        processes.append(Process(target=function_to_be_triggered, args=(i,)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
