import time


def do_nothing_and_gather_times(identification: int):
    print(f'Indentification: {identification}')
    start = time.time()
    res = []
    for i in range(10**6):
        res.append(time.time() - start)
    return res
