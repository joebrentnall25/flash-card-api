"""Main file for FastAPI app"""

from fastapi import FastAPI
from src.api.routes.collection_routes import collection_router
from src.api.routes.card_routes import card_router

app = FastAPI()

base_url = "/v1/"


def init_routers(app_: FastAPI) -> None:
    app_.include_router(collection_router, prefix=base_url+"users/{user_id}/collections")
    app_.include_router(card_router, prefix=base_url+"users/{user_id}/collections/{collection_id}/cards")


def create_app() -> FastAPI:
    app_ = FastAPI(
        title="Hide",
        description="Hide API",
        version="1.0.0"
    )
    init_routers(app_=app_)
    return app_

app = create_app()