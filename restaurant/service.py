from sqlalchemy.orm import Session
from .models import Menu
from .schemas import MenuCreate
from fastapi import HTTPException


def get_menu_list(db: Session):
    return db.query(Menu).all()


def get_menu_id(id, db: Session):
    menu_id = db.query(Menu).get(id)
    if not menu_id:
        raise HTTPException(status_code=404, detail=f"menu item with id {id} not found")
    return menu_id


def create_menu(db: Session, item: MenuCreate):
    menu = Menu(**item.dict())
    db.add(menu)
    db.commit()
    db.refresh(menu)
    return menu


def update_menu(id, db: Session, item: MenuCreate):
    menu_id = db.query(Menu).get(id)
    if not menu_id:
        raise HTTPException(status_code=404, detail=f"menu item with id {id} not found")

    menu_id.title = item.title
    menu_id.description = item.description
    db.commit()
    return menu_id


def delete_menu(id, db: Session):
    menu_id = db.query(Menu).get(id)
    if not menu_id:
        raise HTTPException(status_code=404, detail=f"menu item with id {id} not found")

    db.delete(menu_id)
    db.commit()
    return None