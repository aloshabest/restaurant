from fastapi import APIRouter, Depends, HTTPException
from core.utils import get_db
from sqlalchemy.orm import Session
from . import service
from .schemas import MenuCreate, MenuList
from typing import List
from uuid import UUID


router = APIRouter()


@router.get("/menus", response_model=List[MenuList])
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get("/menus/{menu_id}")
def menu_list(menu_id: int, db: Session = Depends(get_db)):
    return service.get_menu_id(menu_id, db)


@router.post("/menus")
def menu_list(item: MenuCreate, db: Session = Depends(get_db)):
    return service.create_menu(db, item)
