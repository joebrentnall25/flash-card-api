"""Routes for collections"""

from fastapi import APIRouter

collection_router = APIRouter()


@collection_router.get("/", status_code=200)
async def get_all_by_user(user_id):
    """Route to get all collections for a user"""
    return {
        "user": user_id,
        "content": "test"
    }


@collection_router.post("/", status_code=201)
async def create():
    """Creates one or multiple collections"""
    return {
        "message": "success!"
    }
