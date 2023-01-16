from fastapi import APIRouter
from restaurant import rest


routes = APIRouter()

routes.include_router(rest.router, prefix="/api/v1")