from pydantic import BaseModel


class BaseDish(BaseModel):
    id: str
    title: str
    description: str

    class Config:
        orm_mode = True


class DishRequest(BaseModel):
    title: str
    description: str
    price: float


class DishResponse(BaseDish):
    price: str
