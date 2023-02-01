from fastapi import HTTPException
from sqlalchemy.orm import Session

from ..models import Menu, Submenu
from .add_dish import add, add_list
from .schemas import SubmenuRequest


def get_submenu_list(menu_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    submenu = db.query(Submenu).filter_by(menu_id=menu_id).all()
    submenu = add_list(submenu)
    return submenu


def get_submenu_id(menu_id, submenu_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail='submenu not found')
    submenu = add(submenu)
    return submenu


def create_submenu(id, db: Session, item: SubmenuRequest):
    submenu = Submenu(**item.dict())
    submenu.menu_id = id
    db.add(submenu)
    db.commit()
    db.refresh(submenu)
    submenu = add(submenu)
    return submenu


def update_submenu(menu_id, submenu_id, db: Session, item: SubmenuRequest):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail='submenu not found')
    if item.title:
        submenu.title = item.title
    if item.description:
        submenu.description = item.description
    db.commit()
    db.refresh(submenu)
    submenu = add(submenu)
    return submenu


def delete_submenu(menu_id, submenu_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail='menu not found')
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail='submenu not found')
    db.delete(submenu)
    db.commit()
    return None
