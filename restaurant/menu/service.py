from sqlalchemy.orm import Session
from ..models import Menu
from .schemas import MenuResponse
from fastapi import HTTPException
from .add_submenu import add_list, add


def get_menu_list(db: Session):
    menu = db.query(Menu).all()
    menu = add_list(menu)
    return menu


def get_menu_id(id, db: Session):
    menu = db.query(Menu).get(id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
    menu = add(menu)
    return menu


def create_menu(db: Session, item: MenuResponse):
    menu = Menu(**item.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    menu = add(menu)
    return menu


def update_menu(id, db: Session, item: MenuResponse):
    menu = db.query(Menu).get(id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
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
        raise HTTPException(status_code=404, detail=f"menu not found")
    db.delete(menu)
    db.commit()
    return None