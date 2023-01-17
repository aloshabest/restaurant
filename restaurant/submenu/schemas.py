from pydantic import BaseModel


class BaseSubmenu(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True


class SubmenuRequest(BaseModel):
    title: str
    description: str


class SubmenuResponse(BaseSubmenu):
    dishes_count: int
