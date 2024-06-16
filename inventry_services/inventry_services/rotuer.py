from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from typing import List, Annotated
from inventry_services.inventory_model import Category, Product, Inventory
from .schemas import CategoryCreate, CategoryRead, ProductCreate, ProductRead, InventoryCreate, InventoryRead, InventoryUpdate
from .crud import create_category, get_categories, create_product, get_products, get_product, create_inventory_item, get_inventory_item, update_inventory_item, delete_inventory_item
from inventry_services.inventory_db import get_session

router = APIRouter()



# Category routes
@router.post("/categories/")
def create_category_endpoint(category: CategoryCreate, session: Annotated[Session, Depends(get_session)]):
    category =  Category(
        name=category.name,
        description=category.description
    )
    return create_category(session, category)

# @router.get("/categories/", response_model=List[CategoryRead])
# aysnc def get_categories_endpoint(session: Annotated[Session, Depends(get_session)]):
#     return get_categories(session)

# # Product routes
# @router.post("/products/", response_model=ProductRead)
# aysnc def create_product_endpoint(product: ProductCreate, session: Annotated[Session, Depends(get_session)]):
#     product = Product(**product.model_dump())
#     return create_product(session, product)

# @router.get("/products/", response_model=List[ProductRead])
# aysnc def get_products_endpoint( session: Annotated[Session, Depends(get_session)]):
#     return get_products(session)

# @router.get("/products/{product_id}", response_model=ProductRead)
# aysnc def get_product_endpoint(product_id: int, session: Annotated[Session, Depends(get_session)]):
#     product = get_product(session, product_id)
#     if not product:
#         raise HTTPException(status_code=404, detail="Product not found")
#     return product

# # Inventory routes
# @router.post("/inventory/", response_model=InventoryRead)
# aysnc def create_inventory_item_endpoint(inventory_item: InventoryCreate, session: Annotated[Session, Depends(get_session)]):
#     inventory_item = Inventory(**inventory_item.model_dump())
#     return create_inventory_item(session, inventory_item)

# @router.get("/inventory/{item_id}", response_model=InventoryRead)
# aysnc def read_inventory_item_endpoint(item_id: int, session: Annotated[Session, Depends(get_session)]):
#     item = get_inventory_item(session, item_id)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# @router.put("/inventory/{item_id}", response_model=InventoryRead)
# aysnc def update_inventory_item_endpoint(item_id: int, inventory_data: InventoryUpdate, session: Annotated[Session, Depends(get_session)]):
#     item_data = inventory_data.model_dump(exclude_unset=True)
#     item = update_inventory_item(session, item_id, item_data)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

# @router.delete("/inventory/{item_id}")
# aysnc def delete_inventory_item_endpoint(item_id: int, session: Annotated[Session, Depends(get_session)]):
#     success = delete_inventory_item(session, item_id)
#     if not success:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return {"ok": True}
