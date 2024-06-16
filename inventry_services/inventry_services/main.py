

from fastapi import FastAPI
from inventry_services.inventory_db import create_db_table
from inventry_services.rotuer import router
from contextlib import asynccontextmanager

# app = FastAPI()

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     print("Application is starting")
    
#     create_db_table()
#     yield
#     print("table created") 

        



@asynccontextmanager
async def lifespan(app:FastAPI):
    print("Application is starting")
    # task = asyncio.create_task(consume_message(settings.KAFKA_ORDER_TOPIC, settings.KAFKA_BOOTSTRAP_SERVER))
    create_db_table()
    yield
    print("table created") 

        

app:FastAPI = FastAPI(
                    lifespan=lifespan, 
                      title="Todo App",
                        )

app.include_router(router, prefix="/api", tags=["inventory"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(router, prefix="/api", tags=["inventory"])
