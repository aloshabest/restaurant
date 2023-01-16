from pydantic import BaseModel
from typing import Optional
from datetime import datetime


class MenuBase(BaseModel):
    title: str = ''
    text: str = ''


class MenuList(MenuBase):
    id: Optional[int]
    date: Optional[datetime]


class MenuCreate(MenuBase):
    parent_id: Optional[int] = None

    class Config:
        orm_mode = True