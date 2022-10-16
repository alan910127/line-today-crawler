from __future__ import annotations

from typing import Iterable

from .config import settings
from .utils import batch_fetch_jsons


async def fetch_page_info():
    return await batch_fetch_jsons(
        base_url=settings.base_url,
        query_paths=settings.tabs,
        query_params={"country": "tw"},
    )


async def fetch_listings(query_paths: Iterable[str]):
    return await batch_fetch_jsons(
        base_url=settings.listing_base_url,
        query_paths=query_paths,
        query_params={"offset": 0, "length": 5, "country": "tw"},
    )
