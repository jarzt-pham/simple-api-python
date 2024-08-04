from fastapi import APIRouter

router = APIRouter()

@router.get("/items/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

@router.get("/items/item_id", tags=["users"])
async def read_user(item_id: int):
    return {"item_id": item_id}
