from fastapi import APIRouter, Depends
from core.utils import get_db
from sqlalchemy.orm import Session
from . import service
from .schemas import DishRequest, DishResponse
from typing import List


router = APIRouter()


@router.get("/{menu_id}/submenus/{submenu_id}/dishes", response_model=List[DishResponse])
def dish_list(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    return service.get_dish_list(menu_id, submenu_id, db)


@router.get("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=DishResponse)
def dish_list_id(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    return service.get_dish_id(menu_id, submenu_id, dish_id, db)


@router.post("/{menu_id}/submenus/{submenu_id}/dishes", response_model=DishResponse, status_code=201)
def dish_post(submenu_id: int, item: DishRequest, db: Session = Depends(get_db)):
    return service.create_dish(submenu_id, db, item)


@router.patch("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}", response_model=DishResponse)
def dish_update(menu_id: int, submenu_id: int, dish_id: int, item: DishRequest, db: Session = Depends(get_db)):
    return service.update_dish(menu_id, submenu_id, dish_id, db, item)


@router.delete("/{menu_id}/submenus/{submenu_id}/dishes/{dish_id}")
def dish_delete(menu_id: int, submenu_id: int, dish_id: int, db: Session = Depends(get_db)):
    return service.delete_dish(menu_id, submenu_id, dish_id, db)