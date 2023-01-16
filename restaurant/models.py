from core.db import Base
from sqlalchemy import Column, String, Integer, Text, DateTime, Float, ForeignKey
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "Menu"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    date = Column(DateTime)
    submenu = Column(Integer, ForeignKey("Submenu.id"))
    submenu_id = relationship("Submenu")


class Submenu(Base):
    __tablename__ = "Submenu"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    date = Column(DateTime)
    dish = Column(Integer, ForeignKey("Dish.id"))
    dish_id = relationship("Dish")


class Dish(Base):
    __tablename__ = "Dish"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    price = Column(Float)
    date = Column(DateTime)


menus = Menu.__table__