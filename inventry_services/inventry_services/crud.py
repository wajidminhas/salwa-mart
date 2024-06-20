

from typing import Annotated
from fastapi import Depends
from sqlmodel import Session, select

from .inventory_db import get_session
from .inventory_model import Category, Product, Inventory
from datetime import datetime, timedelta, timezone

# Category CRUD operations
"""
    Creates a new category in the database.
    
    Parameters:
        session: Annotated[Session, Depends(get_session)] - the database session
        category: Category - the category object to be added
    
    Returns:
        Category - the newly created category
    """
def create_category(session: Annotated[Session, Depends(get_session)], category: Category):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category


    # ***********     ********************     *************
def get_categories(session: Session):
    return session.exec(select(Category)).all()


     # ***********     ********************     *************
def get_category(session: Session, category_id: int):
    return session.get(Category, category_id)

# Product CRUD operations
def create_product(session: Session, product: Product):
    session.add(product)
    session.commit()
    session.refresh(product)
    return product

     # ***********     ********************     *************
def get_products(session: Session):
    return session.exec(select(Product)).all()

     # ***********     ********************     *************

def get_product(session: Session, product_id: int):
    return session.get(Product, product_id)

     # ***********     ********************     *************

# Inventory CRUD operations
def create_inventory_item(session: Session, inventory_item: Inventory):
    session.add(inventory_item)
    session.commit()
    session.refresh(inventory_item)
    return inventory_item

     # ***********     ********************     *************

def get_inventory_item(session: Session, item_id: int):
    return session.get(Inventory, item_id)


     # ***********     ********************     *************

def update_inventory_item(session: Session, item_id: int, item_data: dict):
    item = session.get(Inventory, item_id)
    if item:
        for key, value in item_data.items():
            setattr(item, key, value)
        item.last_updated = datetime.now(timezone.utc)
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return None

     # ***********     ********************     *************

def delete_inventory_item(session: Session, item_id: int):
    item = session.get(Inventory, item_id)
    if item:
        session.delete(item)
        session.commit()
        return True
    return False
