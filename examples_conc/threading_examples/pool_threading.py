from concurrent.futures import ThreadPoolExecutor


def pool_threading(function_to_be_triggered, length=3):
    with ThreadPoolExecutor() as ex:
        res = ex.map(function_to_be_triggered, range(length))
    return list(res)

