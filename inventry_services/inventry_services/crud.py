from sqlmodel import Session, select
from .models import Item, Category, Supplier, Transaction,StockThreshold

# Category CRUD
def create_category(session: Session, category: Category):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

def get_category(session: Session, category_id: int):
    return session.get(Category, category_id)

# Supplier CRUD
def create_supplier(session: Session, supplier: Supplier):
    session.add(supplier)
    session.commit()
    session.refresh(supplier)
    return supplier

def get_supplier(session: Session, supplier_id: int):
    return session.get(Supplier, supplier_id)

# Item CRUD
def create_item(session: Session, item: Item):
    session.add(item)
    session.commit()
    session.refresh(item)
    return item

def get_item(session: Session, item_id: int):
    return session.get(Item, item_id)

def update_stock_level(session: Session, item_id: int, new_stock_level: int):
    item = session.get(Item, item_id)
    if item:
        item.stock_level = new_stock_level
        session.add(item)
        session.commit()
        session.refresh(item)
        return item
    return None

def delete_item(session: Session, item_id: int):
    item = session.get(Item, item_id)
    if item:
        session.delete(item)
        session.commit()
        return True
    return False

# Transaction CRUD
def create_transaction(session: Session, transaction: Transaction):
    item = session.get(Item, transaction.item_id)
    if not item:
        return None

    if transaction.transaction_type == 'in':
        item.stock_level += transaction.quantity
    elif transaction.transaction_type == 'out':
        if item.stock_level < transaction.quantity:
            raise ValueError("Insufficient stock")
        item.stock_level -= transaction.quantity
    else:
        raise ValueError("Invalid transaction type")

    session.add(transaction)
    session.add(item)
    session.commit()
    session.refresh(transaction)

    # Check if we need to reorder
    check_reorder(session, item)

    return transaction

def get_all_transactions(session: Session):
    return session.exec(select(Transaction)).all()

def delete_transaction(session: Session, transaction_id: int):
    transaction = session.get(Transaction, transaction_id)
    if transaction:
        session.delete(transaction)
        session.commit()
        return True
    return False


def get_transactions_by_item(session: Session, item_id: int):
    statement = select(Transaction).where(Transaction.item_id == item_id)
    results = session.exec(statement)
    return results.all()


def get_stock_threshold(session: Session, item_id: int):
    statement = select(StockThreshold).where(StockThreshold.item_id == item_id)
    return session.exec(statement).first()

def check_reorder(session: Session, item: Item):
    threshold = get_stock_threshold(session, item.id)
    if threshold and item.stock_level < threshold.minimum_level:
        place_order(session, item, threshold)

def place_order(session: Session, item: Item, threshold: StockThreshold):
    order_quantity = max(threshold.maximum_level - item.stock_level, item.reorder_quantity)
    order_transaction = Transaction(
        item_id=item.id,
        transaction_type='in',
        quantity=order_quantity
    )
    item.stock_level += order_quantity
    session.add(order_transaction)
    session.add(item)
    session.commit()
    session.refresh(order_transaction)
    return order_transaction

def create_stock_threshold(session: Session, threshold: StockThreshold):
    session.add(threshold)
    session.commit()
    session.refresh(threshold)
    return threshold

def get_stock_threshold(session: Session, item_id: int):
    statement = select(StockThreshold).where(StockThreshold.item_id == item_id)
    return session.exec(statement).first()
