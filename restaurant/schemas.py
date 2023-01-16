from pydantic import BaseModel


class MenuBase(BaseModel):
    title: str
    description: str

    class Config:
        orm_mode = True


class MenuList(MenuBase):
    id: int


class MenuCreate(MenuBase):
    pass


class MenuUpdate(MenuBase):
    pass
