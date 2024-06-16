

from typing import Optional, List
from pydantic import BaseModel
from datetime import datetime
from sqlmodel import Field, SQLModel

class CategoryCreate(SQLModel):
    name: str
    description: str

class CategoryRead(BaseModel):

    id: int
    name: str

    class Config:
        orm_mode = True

class ProductCreate(BaseModel):
    name: str
    description: Optional[str] = None
    price: float
    category_id: int

class ProductRead(BaseModel):
    id: int
    name: str
    description: Optional[str]
    price: float
    category: CategoryRead

    class Config:
        orm_mode = True

class InventoryCreate(BaseModel):
    product_id: int
    quantity: int
    reorder_level: int

class InventoryUpdate(BaseModel):
    quantity: Optional[int] = None
    reorder_level: Optional[int] = None

class InventoryRead(BaseModel):
    id: int
    product: ProductRead
    quantity: int
    reorder_level: int
    last_updated: datetime

    class Config:
        orm_mode = True
