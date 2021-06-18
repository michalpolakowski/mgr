def cpu_heavy(_: int) -> int:
    count = 0
    for i in range(50000):
        count += i
    return count


async def acpu_heavy(_: int) -> int:
    count = 0
    for i in range(50000):
        count += i
    return count
