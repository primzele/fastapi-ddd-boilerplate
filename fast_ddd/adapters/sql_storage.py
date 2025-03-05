from fast_ddd.domain.value import CreateItem
from fast_ddd.domain.entity import Item
from fast_ddd.domain.repositories.storage import ItemRepository


class SQLStorageAdapter(ItemRepository):

    async def get(self, item_id: int) -> Item:
        # perform actual SQL implementation, query for item with id = id and return Item
        return Item(
            id=item_id,
            name="Sample Item",
            description="Item Description"
        )

    async def save(self, item: CreateItem) -> int:
        # save item to SQL table, return item ID
        return 1
