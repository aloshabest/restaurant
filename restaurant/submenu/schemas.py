from pydantic import BaseModel


class BaseSubmenu(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'id': '2',
                'title': 'My submenu title',
                'description': 'My submenu description',
                'dishes_count': 0,
            },
        }


class SubmenuRequest(BaseModel):
    title: str
    description: str


class SubmenuResponse(BaseSubmenu):
    dishes_count: int
