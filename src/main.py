import asyncio
from typing import Iterable

import httpx
from bs4 import BeautifulSoup

from .config import scaper_settings


async def scrape_htmls(urls: Iterable[str]):
    async with httpx.AsyncClient() as client:
        tasks = (client.get(url) for url in urls)
        responses: list[httpx.Response] = await asyncio.gather(*tasks)
    return [res.text for res in responses]


async def main() -> None:
    htmls = await scrape_htmls(
        f"{scaper_settings.base_url}/{tab}" for tab in scaper_settings.tabs
    )

    all_media: set[str] = set()

    for html in htmls:
        soup = BeautifulSoup(html, "html.parser")

        media_name_elements = soup.find_all(class_="articleMetaInfo-description")

        for element in media_name_elements:
            all_media.add(element.string)

    print("\n".join(sorted(all_media)))


if __name__ == "__main__":
    asyncio.run(main())
