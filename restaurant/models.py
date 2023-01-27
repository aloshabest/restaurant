from sqlalchemy import Column, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import relationship

from core.db import Base


class Menu(Base):
    __tablename__ = 'Menu'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    submenu = relationship('Submenu', cascade='save-update, merge, delete')


class Submenu(Base):
    __tablename__ = 'Submenu'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    menu_id = Column(
        Integer, ForeignKey('Menu.id'),
        nullable=False, index=True,
    )
    menu = relationship('Menu')
    dish = relationship('Dish', cascade='save-update, merge, delete')


class Dish(Base):
    __tablename__ = 'Dish'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    title = Column(String)
    description = Column(Text)
    price = Column(Numeric(scale=2), nullable=False)
    submenu_id = Column(
        Integer, ForeignKey(
            'Submenu.id',
        ), nullable=False, index=True,
    )
    submenu = relationship('Submenu')
