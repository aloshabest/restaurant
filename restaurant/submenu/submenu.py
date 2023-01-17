from fastapi import APIRouter, Depends
from core.utils import get_db
from sqlalchemy.orm import Session
from . import service
from .schemas import SubmenuRequest, SubmenuResponse
from typing import List


router = APIRouter()


@router.get("/{menu_id}/submenus", response_model=List[SubmenuResponse])
def submenu_list(menu_id: int, db: Session = Depends(get_db)):
    return service.get_submenu_list(menu_id, db)


@router.get("/{menu_id}/submenus/{submenu_id}", response_model=SubmenuResponse)
def submenu_list_id(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    return service.get_submenu_id(menu_id, submenu_id, db)


@router.post("/{menu_id}/submenus", response_model=SubmenuResponse, status_code=201)
def submenu_post(menu_id: int, item: SubmenuRequest, db: Session = Depends(get_db)):
    return service.create_submenu(menu_id, db, item)


@router.patch("/{menu_id}/submenus/{submenu_id}", response_model=SubmenuResponse)
def submenu_update(menu_id: int, submenu_id: int, item: SubmenuRequest, db: Session = Depends(get_db)):
    return service.update_submenu(menu_id, submenu_id, db, item)


@router.delete("/{menu_id}/submenus/{submenu_id}")
def submenu_delete(menu_id: int, submenu_id: int, db: Session = Depends(get_db)):
    return service.delete_submenu(menu_id, submenu_id, db)
