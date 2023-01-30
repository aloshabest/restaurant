from pydantic import BaseModel


class BaseMenu(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'id': '1',
                'title': 'My menu title',
                'description': 'My menu description',
                'submenus_count': 0,
                'dishes_count': 0,
            },
        }


class MenuRequest(BaseModel):
    title: str
    description: str


class MenuResponse(BaseMenu):
    submenus_count: int
    dishes_count: int
