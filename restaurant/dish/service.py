from sqlalchemy.orm import Session
from ..models import Menu, Submenu, Dish
from .schemas import DishResponse
from fastapi import HTTPException


def get_dish_list(menu_id, submenu_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
    dish = db.query(Dish).filter_by(submenu_id=submenu_id).all()
    return dish


def get_dish_id(menu_id, submenu_id, dish_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail=f"submenu not found")
    dish = db.query(Dish).get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail=f"dish not found")
    return dish


def create_dish(submenu_id, db: Session, item: DishResponse):
    dish = Dish(**item.dict())
    dish.submenu_id = submenu_id
    db.add(dish)
    db.commit()
    db.refresh(dish)
    return dish


def update_dish(menu_id, submenu_id, dish_id, db: Session, item: DishResponse):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail=f"submenu not found")
    dish = db.query(Dish).get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail=f"dish not found")
    if item.title:
        dish.title = item.title
    if item.description:
        dish.description = item.description
    if item.price:
        dish.price = round(item.price, 2)
    db.commit()
    db.refresh(dish)
    return dish


def delete_dish(menu_id, submenu_id, dish_id, db: Session):
    menu = db.query(Menu).get(menu_id)
    if not menu:
        raise HTTPException(status_code=404, detail=f"menu not found")
    submenu = db.query(Submenu).get(submenu_id)
    if not submenu:
        raise HTTPException(status_code=404, detail=f"submenu not found")
    dish = db.query(Dish).get(dish_id)
    if not dish:
        raise HTTPException(status_code=404, detail=f"dish not found")
    db.delete(dish)
    db.commit()
    return None
