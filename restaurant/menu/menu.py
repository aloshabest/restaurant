from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.cache import *
from core.utils import get_db

from . import service
from .schemas import MenuRequest, MenuResponse

router = APIRouter()


@router.get(path='/', response_model=list[MenuResponse], summary='Get menu list', tags=['Menu'])
def menu_list(db: Session = Depends(get_db)):
    cache = cache_get_list('menus')
    if cache:
        return cache
    menu = service.get_menu_list(db)
    cache_set_list('menus', menu)
    return menu


@router.get(
    path='/{menu_id}', response_model=MenuResponse, summary='Get information about a specific menu',
    tags=['Menu'],
)
def menu_list_id(menu_id: int, db: Session = Depends(get_db)):
    cache = cache_get_item('menu', menu_id)
    if cache:
        return cache
    menu = service.get_menu_id(menu_id, db)
    items = {
        'id': menu.id, 'title': menu.title, 'description': menu.description, 'submenus_count': len(menu.submenu),
        'dishes_count': sum([len(submenu.dish) for submenu in menu.submenu]) if menu.submenu else 0,
    }
    cache_set_item('menu', items)
    return menu


@router.post(
    path='/', response_model=MenuResponse, status_code=201, summary='Create a new menu',
    tags=['Menu'],
)
def menu_post(item: MenuRequest, db: Session = Depends(get_db)):
    menu = service.create_menu(db, item)
    items = {
        'id': menu.id, 'title': menu.title, 'description': menu.description, 'submenus_count': len(menu.submenu),
        'dishes_count': sum([len(submenu.dish) for submenu in menu.submenu]) if menu.submenu else 0,
    }
    cache_set_item('menu', items)
    cache_delete_list('menus')
    return menu


@router.patch(path='/{menu_id}', response_model=MenuResponse, summary='Update a specific menu', tags=['Menu'])
def menu_update(menu_id: int, item: MenuRequest, db: Session = Depends(get_db)):
    menu = service.update_menu(menu_id, db, item)
    items = {
        'id': menu.id, 'title': menu.title, 'description': menu.description, 'submenus_count': len(menu.submenu),
        'dishes_count': sum([len(submenu.dish) for submenu in menu.submenu]) if menu.submenu else 0,
    }
    cache_set_item('menu', items)
    cache_delete_list('menus')
    return menu


@router.delete(path='/{menu_id}', summary='Delete a specific menu', tags=['Menu'])
def menu_delete(menu_id: int, db: Session = Depends(get_db)):
    menu = service.delete_menu(menu_id, db)
    cache_delete_item('menu', menu_id)
    cache_delete_list('menus')
    return menu
