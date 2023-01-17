from fastapi import APIRouter, Depends
from core.utils import get_db
from sqlalchemy.orm import Session
from . import service
from .schemas import MenuRequest, MenuResponse
from typing import List


router = APIRouter()


@router.get("/", response_model=List[MenuResponse])
def menu_list(db: Session = Depends(get_db)):
    return service.get_menu_list(db)


@router.get("/{menu_id}", response_model=MenuResponse)
def menu_list_id(menu_id: int, db: Session = Depends(get_db)):
    return service.get_menu_id(menu_id, db)


@router.post("/", response_model=MenuResponse, status_code=201)
def menu_post(item: MenuRequest, db: Session = Depends(get_db)):
    return service.create_menu(db, item)


@router.patch("/{menu_id}", response_model=MenuResponse)
def menu_update(menu_id: int, item: MenuRequest, db: Session = Depends(get_db)):
    return service.update_menu(menu_id, db, item)


@router.delete("/{menu_id}")
def menu_delete(menu_id: int, db: Session = Depends(get_db)):
    return service.delete_menu(menu_id, db)