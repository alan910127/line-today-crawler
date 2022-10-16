from __future__ import annotations

import asyncio
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Awaitable, Callable, ParamSpec, TypeVar

    P = ParamSpec("P")
    R = TypeVar("R")


def make_sync(func: Callable[P, Awaitable[R]]) -> Callable[P, R]:
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        return asyncio.run(func(*args, **kwargs))

    return wrapper
