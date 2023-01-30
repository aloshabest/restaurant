from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.cache import *
from core.utils import get_db

from . import service
from .schemas import SubmenuRequest, SubmenuResponse

router = APIRouter()


@router.get('/{menu_id}/submenus', response_model=list[SubmenuResponse])
def submenu_list(menu_id: int, db: Session = Depends(get_db)):
    cache = cache_get_list('submenus')
    if cache:
        return cache
    submenu = service.get_submenu_list(menu_id, db)
    cache_set_list('submenus', submenu)
    return submenu


@router.get('/{menu_id}/submenus/{submenu_id}', response_model=SubmenuResponse)
def submenu_list_id(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    cache = cache_get_item('submenu', submenu_id)
    if cache:
        return cache
    submenu = service.get_submenu_id(menu_id, submenu_id, db)
    items = {
        'id': submenu.id, 'title': submenu.title, 'description': submenu.description,
        'dishes_count': len(submenu.dish),
    }
    cache_set_item('submenu', items)
    return submenu


@router.post('/{menu_id}/submenus', response_model=SubmenuResponse, status_code=201)
def submenu_post(menu_id: int, item: SubmenuRequest, db: Session = Depends(get_db)):
    submenu = service.create_submenu(menu_id, db, item)
    items = {
        'id': submenu.id, 'title': submenu.title, 'description': submenu.description,
        'dishes_count': len(submenu.dish),
    }
    cache_set_item('submenu', items)
    cache_delete_list('submenus')
    cache_delete_list('menus')
    cache_delete_item('menu', menu_id)
    return submenu


@router.patch('/{menu_id}/submenus/{submenu_id}', response_model=SubmenuResponse)
def submenu_update(menu_id: int, submenu_id: int, item: SubmenuRequest, db: Session = Depends(get_db)):
    submenu = service.update_submenu(menu_id, submenu_id, db, item)
    items = {
        'id': submenu.id, 'title': submenu.title, 'description': submenu.description,
        'dishes_count': len(submenu.dish),
    }
    cache_set_item('submenu', items)
    cache_delete_list('submenus')
    return submenu


@router.delete('/{menu_id}/submenus/{submenu_id}')
def submenu_delete(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    submenu = service.delete_submenu(menu_id, submenu_id, db)
    cache_delete_item('submenu', submenu_id)
    cache_delete_list('submenus')
    cache_delete_list('menus')
    cache_delete_item('menu', menu_id)
    return submenu
