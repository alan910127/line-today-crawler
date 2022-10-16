"""Mimicked database operations for storing publishers"""
from __future__ import annotations

from pathlib import Path
from typing import Iterable


def store_publishers(output_file: Path, publisher_names: Iterable[str]):
    """Update the content in ``output_file`` by adding ``publisher_names`` without repeating"""

    if output_file.exists():
        with output_file.open("r") as file:
            current_stored = {name.strip() for name in file}
    else:
        current_stored: set[str] = set()

    current_stored.update(publisher_names)

    with output_file.open("w") as file:  # truncate all
        file.write("\n".join(sorted(current_stored)))
