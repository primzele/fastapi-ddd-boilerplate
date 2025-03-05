from fast_ddd.domain.repositories.storage import ItemRepository
from fast_ddd.domain.entity import Item
from fast_ddd.domain.value import CreateItem


class ItemsManager(object):
    storage = None

    def __init__(self, storage: ItemRepository):
        self.storage = storage

    async def get(self, item_id: int) -> Item:
        return await self.storage.get(item_id=item_id)

    async def save(self, item: CreateItem) -> int:
        return await self.storage.save(item=item)
