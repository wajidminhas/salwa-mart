from pydantic import BaseModel
from typing import Optional, List
from datetime import datetime

class CategoryCreate(BaseModel):
    name: str
    description: Optional[str] = None

class CategoryRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None

    class Config:
        orm_mode = True

class SupplierCreate(BaseModel):
    name: str
    contact_info: Optional[str] = None

class SupplierRead(BaseModel):
    id: int
    name: str
    contact_info: Optional[str] = None

    class Config:
        orm_mode = True

class ItemCreate(BaseModel):
    name: str
    description: Optional[str] = None
    stock_level: int
    category_id: Optional[int]
    supplier_id: Optional[int]

class ItemRead(BaseModel):
    id: int
    name: str
    description: Optional[str] = None
    stock_level: int
    category_id: Optional[int]
    supplier_id: Optional[int]

    class Config:
        orm_mode = True

class TransactionCreate(BaseModel):
    item_id: int
    transaction_type: str
    quantity: int

class TransactionRead(BaseModel):
    id: int
    item_id: int
    transaction_type: str
    quantity: int
    timestamp: datetime

    class Config:
        orm_mode = True
