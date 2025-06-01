from __future__ import annotations
from collections.abc import Iterator
from typing import Any
import random


class RandomOrderIterator(Iterator):
    _position: int = None

    def __init__(self, collection: list[Any], ) -> None:
        self._collection = random.sample(collection, len(collection))
        self._position = 0

    def __next__(self) -> Any:
        try:
            value = self._collection[self._position]
            self._position += 1
        except IndexError:
            raise StopIteration()

        return value
