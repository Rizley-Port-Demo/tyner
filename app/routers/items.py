from fastapi import APIRouter
from pydantic import BaseModel
router = APIRouter()
class Item(BaseModel):
    name: str
    description: str | None = None
@router.get("/")
def list_items():
    return []
@router.post("/")
def create_item(item: Item):
    return item
