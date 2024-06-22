

# Inventory Management System

This project is an Inventory Management System built with Python, SQLModel, and FastAPI. It includes functionalities for managing stock levels, updating inventory, and automatically generating orders to suppliers when stock levels fall below certain thresholds.

## Features

- Manage categories, suppliers, items, and transactions
- Automatic stock level updates
- Automatic reorder generation for suppliers based on stock thresholds

## Requirements

- Python 3.7+
- Poetry
- PostgreSQL

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/yourusername/inventory-management-system.git
    cd inventory-management-system
    ```

2. Install Poetry if you don't have it:

    ```sh
    curl -sSL https://install.python-poetry.org | python3 -
    ```

3. Install the dependencies using Poetry:

    ```sh
    poetry install
    ```

4. Configure the database URL:

    Create a `.env` file in the root directory of the project and add the following line, replacing the placeholder with your actual database URL:

    ```sh
    DATABASE_URL="postgresql://username:password@host/dbname?sslmode=require"
    ```

5. Initialize the database with Alembic:

    ```sh
    poetry run alembic upgrade head
    ```

## Project Structure

```plaintext
inventory-management-system/
├── alembic/                # Alembic migrations directory
│   └── versions/           # Alembic migration scripts
├── models.py               # SQLModel schemas
├── crud.py                 # CRUD operations
├── main.py                 # FastAPI application
├── requirements.txt        # Python dependencies
├── pyproject.toml          # Poetry configuration file
├── alembic.ini             # Alembic configuration file
└── README.md               # Project documentation


## Running the Application
# To run the FastAPI application, use the following command:

    poetry run uvicorn main:app --reload

# the application will be available at http://127.0.0.1:8000.


### Summary

- **Project structure:** Provides a clear overview of the project structure.
- **Installation instructions:** Details how to set up the environment, install dependencies using Poetry, and configure the database URL.
- **Model schemas:** Describes the database models and their relationships.
- **CRUD operations:** Outlines the functions for creating, reading, and updating data.
- **Main application:** Shows how to set up and run the FastAPI application.
- **Running the application:** Includes instructions for running the server using Poetry.
