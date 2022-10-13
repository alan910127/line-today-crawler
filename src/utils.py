import asyncio
import json
from pathlib import Path
from typing import Any, Iterable

import httpx


async def batch_fetch_jsons(
    base_url: str,
    query_paths: Iterable[str],
    query_params: httpx.QueryParams = None,
):
    """Return the json response by hitting the endpoints specified in parameters.
    Endpoints are in the format of `{base_url}/{query_path}`.
    """

    async with httpx.AsyncClient() as client:
        tasks = (
            client.get(f"{base_url}/{url}", params=query_params) for url in query_paths
        )
        responses: list[httpx.Response] = await asyncio.gather(
            *tasks, return_exceptions=True
        )

    return [
        res.json()
        for res in responses
        if isinstance(res, httpx.Response) and res.is_success
    ]


def extract_query_paths(info_json: dict[str, Any]):
    query_paths: list[str] = []

    module: dict[str, Any]
    for module in info_json["modules"]:
        query_paths.extend(entry["id"] for entry in module.get("listings", []))

    return query_paths


def extract_publishers(listing_entry: dict[str, Any]) -> list[str]:
    """Extract the publishers' names from the ``listing_entry``, i.e. response of ``{listing_base_url}/{tab_name}``"""

    return [item["publisher"] for item in listing_entry["items"] if "publisher" in item]


def output_json_file(json_data: Any, output_path: Path, **kwargs):
    with output_path.open("w") as json_file:
        json.dump(json_data, json_file, ensure_ascii=False, indent=4, **kwargs)
