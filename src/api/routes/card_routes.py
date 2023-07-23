"""Routes for card"""

from fastapi import APIRouter

card_router = APIRouter()


@card_router.get("/", status_code=200)
async def get_all_by_collection(user_id: str, collection_id: str):
    """Route for getting all cards by collection_id"""

    return {
        "userId": user_id,
        "collectionId": collection_id
    }


@card_router.get("/{card_id}", status_code=200)
async def get_by_id(user_id: str, collection_id: str, card_id: str):
    """Route for getting card by card_id"""

    return {
        "userId": user_id,
        "collectionId": collection_id,
        "cardId": card_id
    }


@card_router.post("/", status_code=201)
async def create():
    """Create one or multiple cards"""

    return {
        "message": "success!"
    }
