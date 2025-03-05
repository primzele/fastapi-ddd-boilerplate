from fastapi import APIRouter, Depends

from fast_ddd.adapters.sql_storage import SQLStorageAdapter
from fast_ddd.domain.repositories.storage import ItemRepository
from fast_ddd.domain.value import CreateItem
from fast_ddd.interfaces.rest.dto.request import CreateItemRequest
from fast_ddd.interfaces.rest.dto.response import CreatedItemDTO, ItemDTO
from fast_ddd.services.items.items_manager import ItemsManager

router = APIRouter()


def get_storage() -> ItemRepository:
    return SQLStorageAdapter()


@router.post("/create/", response_model=CreatedItemDTO)
async def create(item: CreateItemRequest, storage: ItemRepository = Depends(get_storage)):
    service: ItemsManager = ItemsManager(storage=storage)

    created_item_id: int = await service.save(item=CreateItem(
        name=item.name,
        description=item.description,
    ))

    return {"id": created_item_id}


@router.get("/get/{id}/", response_model=ItemDTO)
async def get(id: int, storage: ItemRepository = Depends(get_storage)):
    service: ItemsManager = ItemsManager(storage=storage)

    return await service.get(item_id=id)
