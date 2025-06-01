from __future__ import annotations
from collections.abc import Iterator
from agents import Agent, AgentAntiTrend, AgentCustom, AgentTrend
import random


class RandomOrderIterator(Iterator):
    _position: int = None

    def __init__(
        self,
        collection: list[Agent | AgentTrend | AgentAntiTrend | AgentCustom],
    ) -> None:
        self._collection = random.sample(collection, len(collection))
        self._position = 0

    def __next__(self) -> Agent | AgentTrend | AgentAntiTrend | AgentCustom:
        try:
            agent = self._collection[self._position]
            self._position += 1
            agent.turn = self._position
        except IndexError:
            raise StopIteration()

        return agent
