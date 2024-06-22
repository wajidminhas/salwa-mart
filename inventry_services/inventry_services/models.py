from sqlmodel import Field, SQLModel, Relationship
from typing import Optional, List
from datetime import datetime

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # description: Optional[str] = None
    items: List["Item"] = Relationship(back_populates="category")

class Supplier(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    contact_info: Optional[str] = None
    items: List["Item"] = Relationship(back_populates="supplier")
    # email: str


class Item(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    stock_level: int
    reorder_threshold: int
    reorder_quantity: int
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    supplier_id: Optional[int] = Field(default=None, foreign_key="supplier.id")
    category: Optional[Category] = Relationship(back_populates="items")
    supplier: Optional[Supplier] = Relationship(back_populates="items")
    transactions: List["Transaction"] = Relationship(back_populates="item")
    threshold: Optional["StockThreshold"] = Relationship(back_populates="item")


class Transaction(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_id: Optional[int] = Field(default=None, foreign_key="item.id")
    transaction_type: str  # 'in' for stock-in, 'out' for stock-out
    quantity: int
    timestamp: datetime = Field(default_factory=datetime.utcnow)
    item: Optional[Item] = Relationship(back_populates="transactions")

class StockThreshold(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    item_id: int = Field(default=None, foreign_key="item.id")
    minimum_level: int
    maximum_level: int
    item: Optional[Item] = Relationship(back_populates="threshold")