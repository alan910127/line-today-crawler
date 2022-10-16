from __future__ import annotations

from pathlib import Path

from .db import store_publishers
from .decorator import make_sync
from .service import fetch_listings, fetch_page_info
from .utils import extract_publishers, extract_query_paths


@make_sync
async def main() -> None:
    # fetch all informations from line today api
    page_info_json = await fetch_page_info()

    # extract listings query paths in each complete information
    listings_query_paths: list[str] = []
    for page_info in page_info_json:
        listings_query_paths.extend(extract_query_paths(page_info))

    # fetch listings (w/ id, type, items)
    listings_json = await fetch_listings(listings_query_paths)

    # extract publisher names from listings
    publisher_names: list[str] = []
    for listing_entry in listings_json:
        publisher_names.extend(extract_publishers(listing_entry))

    # store the result of fetched publisher names
    output_path = Path("output") / "publishers.txt"
    store_publishers(output_path, publisher_names)


if __name__ == "__main__":
    main()
