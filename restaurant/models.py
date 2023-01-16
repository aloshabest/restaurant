from core.db import Base
from sqlalchemy import Column, String, Integer, Text, Float, ForeignKey
from sqlalchemy.orm import relationship


class Menu(Base):
    __tablename__ = "Menu"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    submenu = relationship("Submenu", cascade='save-update, merge, delete')


class Submenu(Base):
    __tablename__ = "Submenu"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    menu_id = Column(Integer, ForeignKey("Menu.id"), nullable=False, index=True)
    menu = relationship("Menu")
    dish = relationship("Dish", cascade='save-update, merge, delete')


class Dish(Base):
    __tablename__ = "Dish"
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String, unique=True)
    description = Column(Text)
    price = Column(Float)
    submenu_id = Column(Integer, ForeignKey("Submenu.id"), nullable=False, index=True)
    submenu = relationship("Submenu")


menus = Menu.__table__