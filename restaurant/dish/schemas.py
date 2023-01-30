from pydantic import BaseModel


class BaseDish(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True
        schema_extra = {
            'example': {
                'id': '3',
                'title': 'My dish title',
                'description': 'My dish description',
                'price': '10.00',
            },
        }


class DishRequest(BaseModel):
    title: str
    description: str
    price: float


class DishResponse(BaseDish):
    price: str
