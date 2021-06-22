import asyncio
from typing import Callable, Awaitable, Union, List, Tuple

import aiohttp


async def asyncio_main(args,
                       function_to_be_triggered: Union[
                           Callable[[int, aiohttp.ClientSession], Awaitable[Tuple[float, float]]],
                           Callable[[int], Awaitable[Tuple[float, float]]]
                       ],
                       length=10):
    tasks = []
    if args.io:
        async with aiohttp.ClientSession() as session:
            for i in range(length):
                tasks.append(function_to_be_triggered(i, session))

            return await asyncio.gather(*tasks)
    else:
        for i in range(length):
            tasks.append(function_to_be_triggered(i))

        return await asyncio.gather(*tasks)
