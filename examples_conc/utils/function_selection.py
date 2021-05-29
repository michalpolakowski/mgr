from argparse import Namespace
from typing import Callable

from utils.cpu_heavy import cpu_heavy
from utils.downloading_pages import download_all_sites
from utils.mocks import do_nothing_and_gather_times


def function_selection(args: Namespace) -> Callable:
    if args.real_time:
        return do_nothing_and_gather_times
    elif args.io:
        return download_all_sites
    return cpu_heavy
