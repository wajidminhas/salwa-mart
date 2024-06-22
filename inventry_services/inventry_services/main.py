from typing import List
from fastapi import FastAPI, Depends, HTTPException
from contextlib import asynccontextmanager
from sqlmodel import Session
from .database import create_db_table, get_session
from .models import Item, Category, Supplier, Transaction, StockThreshold
from .schemas import ItemCreate, ItemRead, ItemUpdate, CategoryCreate, CategoryRead, SupplierCreate, StockThresholdRead, SupplierRead, TransactionCreate, TransactionRead, TransactionUpdate, StockThresholdCreate
from .crud import create_item, delete_transaction, get_all_transactions, get_item, update_stock_level, delete_item, create_category, get_category, create_supplier, get_supplier, create_transaction, get_transactions_by_item, create_stock_threshold, get_stock_threshold




@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Creating database tables...")
    create_db_table()
    yield
    print("Closing database connection...")

app = FastAPI(lifespan=lifespan, title="Inventry Service API")


# ***************** START OF CATEGORIES ENDPOINTS **********************

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

     # *************** END OF CATEGORIES **********************


    # ***************** START OF Supplier ENDPOINTS **********************


# Supplier endpoints
@app.post("/suppliers/", response_model=SupplierRead)
def create_new_supplier(supplier: SupplierCreate, session: Session = Depends(get_session)):
    db_supplier = create_supplier(session, Supplier(**supplier.dict()))
    return db_supplier

@app.put("/suppliers/{supplier_id}", response_model=SupplierRead)
def update_supplier(supplier_id: int, supplier: SupplierCreate, session: Session = Depends(get_session)):
    db_supplier = get_supplier(session, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

@app.delete("/suppliers/{supplier_id}")
def delete_supplier(supplier_id: int, session: Session = Depends(get_session)):
    if delete_supplier(session, supplier_id):
        return {"deleted": True}
    return {"deleted": False}

@app.get("/suppliers/{supplier_id}", response_model=SupplierRead)
def read_supplier(supplier_id: int, session: Session = Depends(get_session)):
    db_supplier = get_supplier(session, supplier_id)
    if db_supplier is None:
        raise HTTPException(status_code=404, detail="Supplier not found")
    return db_supplier

    # *************** END OF SUPPLIER ENDPOINTS **********************


    # *************** START OF ITEM ENDPOINTS **********************

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


# *************** END OF ITEM ENDPOINTS **********************


# *************** START OF TRANSACTION ENDPOINTS **********************

# Transaction endpoints
@app.post("/transactions/", response_model=TransactionRead)
def create_new_transaction(transaction: TransactionCreate, session: Session = Depends(get_session)):
    db_transaction = create_transaction(session, Transaction(**transaction.dict()))
    return db_transaction

@app.get("/items/{item_id}/transactions/", response_model=List[TransactionRead])
def read_transactions_by_item(item_id: int, session: Session = Depends(get_session)):
    db_transactions = get_transactions_by_item(session, item_id)
    return db_transactions

@app.get("/transactions", response_model=TransactionRead)
def read_all_transactions(session: Session = Depends(get_session)):
    db_transactions = get_all_transactions(session)
    return db_transactions

@app.delete("/transactions/{transaction_id}")
def delete_existing_transaction(transaction_id: int, session: Session = Depends(get_session)):
    success = delete_transaction(session, transaction_id)
    if not success:
        raise HTTPException(status_code=404, detail="Transaction not found")
    return {"ok": True}


# *************** END OF TRANSACTION ENDPOINTS **********************


# Stock Threshold endpoints
@app.post("/stock_thresholds/", response_model=StockThresholdRead)
def create_new_stock_threshold(threshold: StockThresholdCreate, session: Session = Depends(get_session)):
    db_threshold = create_stock_threshold(session, StockThreshold(**threshold.dict()))
    return db_threshold

@app.get("/stock_thresholds/{item_id}", response_model=StockThresholdRead)
def read_stock_threshold(item_id: int, session: Session = Depends(get_session)):
    db_threshold = get_stock_threshold(session, item_id)
    if db_threshold is None:
        raise HTTPException(status_code=404, detail="Stock threshold not found")
    return db_threshold