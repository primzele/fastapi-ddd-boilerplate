from fastapi import FastAPI
from fast_ddd.interfaces.rest.routers.items import router as items_router

app = FastAPI()

app.include_router(items_router, prefix="/items")