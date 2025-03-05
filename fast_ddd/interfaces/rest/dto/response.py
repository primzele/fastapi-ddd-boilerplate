from pydantic import BaseModel


class CreatedItemDTO(BaseModel):
    id: int


class ItemDTO(BaseModel):
    id: int
    name: str
    description: str | None = None
