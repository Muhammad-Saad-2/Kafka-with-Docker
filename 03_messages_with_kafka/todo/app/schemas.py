from pydantic import BaseModel

class OrderCreate(BaseModel):
    item_name: str
    quantity: int

class Order(OrderCreate):
    id: int

    class Config:
        orm_mode = True
