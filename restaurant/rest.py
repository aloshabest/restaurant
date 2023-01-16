from fastapi import APIRouter, Depends, HTTPException
from core.utils import get_db
from sqlalchemy.orm import Session
from . import service
from .schemas import MenuCreate, MenuList, MenuUpdate
from typing import List
from uuid import UUID


router = APIRouter()


@router.get("/menus", response_model=List[MenuList])
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get("/menus/{menu_id}")
def menu_list_id(menu_id: int, db: Session = Depends(get_db)):
    return service.get_menu_id(menu_id, db)


@router.post("/menus")
def menu_post(item: MenuCreate, db: Session = Depends(get_db)):
    return service.create_menu(db, item)


@router.put("/menus/{menu_id}")
def menu_update(menu_id: int, item: MenuUpdate, db: Session = Depends(get_db)):
    return service.update_menu(menu_id, db, item)


@router.delete("/menus/{menu_id}")
def menu_delete(menu_id: int, db: Session = Depends(get_db)):
    return service.delete_menu(menu_id, db)