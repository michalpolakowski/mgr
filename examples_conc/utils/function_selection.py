from argparse import Namespace
from typing import Callable

from utils.cpu_heavy import cpu_heavy
from utils.downloading_pages import download_all_sites
from utils.mocks import do_nothing_and_gather_times
from utils.downloading_pages import asyncio_download_all_sites
from utils.cpu_heavy import acpu_heavy
from utils.mocks import ado_nothing_and_gather_times


def function_selection(args: Namespace) -> Callable:
    if args.real_time:
        if args.level == 'asyncio':
            return ado_nothing_and_gather_times
        return do_nothing_and_gather_times
    elif args.io:
        if args.level == 'asyncio':
            return asyncio_download_all_sites
        return download_all_sites
    if args.level == 'asyncio':
        return acpu_heavy
    return cpu_heavy
