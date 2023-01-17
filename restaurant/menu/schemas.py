from pydantic import BaseModel


class BaseMenu(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True


class MenuRequest(BaseModel):
    title: str
    description: str


class MenuResponse(BaseMenu):
    submenus_count: int
    dishes_count: int
