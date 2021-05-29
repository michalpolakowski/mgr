from threading import Thread


def simple_threading(function_to_be_triggered, length=10):
    processes = []
    for i in range(length):
        processes.append(Thread(target=function_to_be_triggered, args=(i,)))
    for process in processes:
        process.start()
    for process in processes:
        process.join()
