from concurrent.futures import ProcessPoolExecutor


def pool_processing(function_to_be_triggered, length=10):
    with ProcessPoolExecutor() as ex:
        res = ex.map(function_to_be_triggered, range(length))
    return list(res)
