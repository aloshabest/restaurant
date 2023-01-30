from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from core.cache import *
from core.utils import get_db

from . import service
from .schemas import DishRequest, DishResponse

router = APIRouter()


@router.get('/{menu_id}/submenus/{submenu_id}/dishes', response_model=list[DishResponse])
def dish_list(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    cache = cache_get_list('dishes')
    if cache:
        return cache
    dish = service.get_dish_list(menu_id, submenu_id, db)
    cache_set_list('dishes', dish)
    return dish


@router.get('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishResponse)
def dish_list_id(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    cache = cache_get_item('dish', dish_id)
    if cache:
        return cache
    dish = service.get_dish_id(menu_id, submenu_id, dish_id, db)
    items = {
        'id': dish.id, 'title': dish.title,
        'description': dish.description, 'price': str(dish.price),
    }
    cache_set_item('dish', items)
    return dish


@router.post('/{menu_id}/submenus/{submenu_id}/dishes', response_model=DishResponse, status_code=201)
def dish_post(submenu_id: int, item: DishRequest, db: Session = Depends(get_db)):
    dish = service.create_dish(submenu_id, db, item)
    items = {
        'id': dish.id, 'title': dish.title,
        'description': dish.description, 'price': str(dish.price),
    }
    cache_set_item('dish', items)
    cache_delete_list('submenus')
    cache_delete_list('menus')
    cache_delete_list('dishes')
    cache_delete_item('submenu', submenu_id)
    return dish


@router.patch('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}', response_model=DishResponse)
def dish_update(menu_id: int, submenu_id: int, dish_id: int, item: DishRequest, db: Session = Depends(get_db)):
    dish = service.update_dish(menu_id, submenu_id, dish_id, db, item)
    items = {
        'id': dish.id, 'title': dish.title,
        'description': dish.description, 'price': str(dish.price),
    }
    cache_set_item('dish', items)
    cache_delete_list('dishes')
    return dish


@router.delete('/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}')
def dish_delete(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    dish = service.delete_dish(menu_id, submenu_id, dish_id, db)
    cache_delete_item('dish', dish_id)
    cache_delete_list('submenus')
    cache_delete_list('menus')
    cache_delete_list('dishes')
    cache_delete_item('submenu', submenu_id)
    cache_delete_item('menu', menu_id)
    return dish
