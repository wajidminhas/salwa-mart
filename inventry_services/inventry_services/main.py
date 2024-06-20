from fastapi import FastAPI, Depends, HTTPException
from sqlmodel import Session
from .database import init_db, get_session
from .models import Item, Category, Supplier, Transaction
from .schemas import ItemCreate, ItemRead, ItemUpdate, CategoryCreate, CategoryRead, SupplierCreate, SupplierRead, TransactionCreate, TransactionRead
from .crud import create_item, get_item, update_stock_level, delete_item, create_category, get_category, create_supplier, get_supplier, create_transaction, get_transactions_by_item

app = FastAPI()

@app.on_event("startup")
def on_startup():
    init_db()

# Category endpoints
@app.post("/categories/", response_model=CategoryRead)
def create_new_category(category: CategoryCreate, session: Session = Depends(get_session)):
    db_category = create_category(session, Category(**category.dict()))
    return db_category

@app.get("/categories/{category_id}", response_model=CategoryRead)
def read_category(category_id: int, session: Session = Depends(get_session)):
    db_category = get_category(session, category_id)
    if db_category is None:
        raise HTTPException(status_code=404, detail="Category not found")
    return db_category

# Supplier endpoints
@app.post("/suppliers/", response_model=SupplierRead)
def create_new_supplier(supplier: SupplierCreate, session: Session = Depends(get_session)):
    db_supplier = create_supplier(session, Supplier(**supplier.dict()))
    return db_supplier

@app.get("/suppliers/{supplier_id}", response_model=SupplierRead)
def read_supplier(supplier_id: int, session: Session = Depends(get_session)):
    db_supplier = get_supplier(session, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

# Item endpoints
@app.post("/items/", response_model=ItemRead)
def create_new_item(item: ItemCreate, session: Session = Depends(get_session)):
    db_item = create_item(session, Item(**item.dict()))
    return db_item

@app.get("/items/{item_id}", response_model=ItemRead)
def read_item(item_id: int, session: Session = Depends(get_session)):
    db_item = get_item(session, item_id)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.put("/items/{item_id}", response_model=ItemRead)
def update_item_stock(item_id: int, item: ItemUpdate, session: Session = Depends(get_session)):
    db_item = update_stock_level(session, item_id, item.stock_level)
    if db_item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return db_item

@app.delete("/items/{item_id}")
def delete_existing_item(item_id: int, session: Session = Depends(get_session)):
    success = delete_item(session, item_id)
    if not success:
        raise HTTPException(status_code=404, detail="Item not found")
    return {"ok": True}

# Transaction endpoints
@app.post("/transactions/", response_model=TransactionRead)
def create_new_transaction(transaction: TransactionCreate, session: Session = Depends(get_session)):
    db_transaction = create_transaction(session, Transaction(**transaction.dict()))
    return db_transaction

# @app.get("/items/{item_id}/transactions/", response_model=List[TransactionRead])
# def read_transactions
