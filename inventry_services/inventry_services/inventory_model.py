from sqlmodel import SQLModel, Field, Relationship
from typing import Optional, List
from datetime import datetime

class Category(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    # description: Optional[str] = None
    products: List["Product"] = Relationship(back_populates="category")

class Product(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    description: Optional[str] = None
    price: float
    category_id: Optional[int] = Field(default=None, foreign_key="category.id")
    category: Optional[Category] = Relationship(back_populates="products")
    inventory_items: List["Inventory"] = Relationship(back_populates="product")

class Inventory(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    quantity: int
    reorder_level: int
    last_updated: datetime = Field(default_factory=datetime.utcnow)
    product: Product = Relationship(back_populates="inventory_items")

class Order(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    product_id: int = Field(foreign_key="product.id")
    quantity: int
    order_date: datetime = Field(default_factory=datetime.utcnow)
    product: Product = Relationship()
