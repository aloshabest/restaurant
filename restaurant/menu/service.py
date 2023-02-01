from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models import Menu
from .add_submenu import add, add_list
from .schemas import MenuRequest


def get_menu_list(db: Session):
    menu = db.query(Menu).all()
    menu = add_list(menu)
    return menu


def get_menu_id(id, db: Session):
    menu = db.query(Menu).get(id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    menu = add(menu)
    return menu


def create_menu(db: Session, item: MenuRequest):
    menu = Menu(**item.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    menu = add(menu)
    return menu


def update_menu(id, db: Session, item: MenuRequest):
    menu = db.query(Menu).get(id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    if item.title:
        menu.title = item.title
    if item.description:
        menu.description = item.description
    db.commit()
    db.refresh(menu)
    menu = add(menu)
    return menu


def delete_menu(id, db: Session):
    menu = db.query(Menu).get(id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    db.delete(menu)
    db.commit()
    return None
