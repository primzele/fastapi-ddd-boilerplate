from typing import Protocol

from fast_ddd.domain.entity import Item
from fast_ddd.domain.value import CreateItem


class ItemRepository(Protocol):
    async def get(self, item_id: int) -> Item:
        raise NotImplementedError

    async def save(self, item: CreateItem) -> int:
        raise NotImplementedError
