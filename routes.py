from fastapi import APIRouter
from restaurant.menu import menu
from restaurant.submenu import submenu
from restaurant.dish import dish

routes = APIRouter()

routes.include_router(menu.router, prefix="/api/v1/menus")
routes.include_router(submenu.router, prefix="/api/v1/menus")
routes.include_router(dish.router, prefix="/api/v1/menus")