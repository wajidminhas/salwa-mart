

from fastapi import FastAPI
from inventry_services.inventory_db import create_db_table
from .rotuer import router
from contextlib import asynccontextmanager

# app = FastAPI()

# @asynccontextmanager
# async def lifespan(app:FastAPI):
#     print("Application is starting")
    
#     create_db_table()
#     yield
#     print("table created") 

        



@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Context manager for the FastAPI lifespan events.

    This function is executed when the application starts and stops.
    It creates the database table and prints a message when the application starts and stops.

    Args:
        app (FastAPI): The FastAPI application.

    Yields:
        None
    """
    # Print a message when the application starts
    print("Application is starting")

    # Create the database table
    create_db_table()

    # Yield control to the application
    yield

    # Print a message when the application stops
    print("table created")

        

app:FastAPI = FastAPI(lifespan=lifespan)

app.include_router(router, prefix="/api", tags=["inventory"])

@app.get("/")
def read_root():
    return {"Hello": "World"}


# app.include_router(router, prefix="/api", tags=["inventory"])
