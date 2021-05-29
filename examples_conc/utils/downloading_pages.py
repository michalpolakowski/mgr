from typing import Tuple

import requests
import time


def download_site(url: str, session: requests.Session) -> None:
    with session.get(url):
        pass


def download_all_sites(x: int) -> Tuple[float, float]:
    print(f'Identification: {x}')
    sites = [
        "https://www.python.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start = time.time()
    with requests.Session() as session:
        for url in sites:
            download_site(url, session)
    stop = time.time()
    print(f"Downloaded {len(sites)} in {stop - start} seconds")
    return start, stop
