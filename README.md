# Cosmocloud_ecommerce

# Ecommerce Application

This is a sample backend application built with FastAPI and MongoDB. It provides APIs for an ecommerce application similar to Flipkart or Amazon. The application allows listing products, creating orders, fetching orders, updating product quantities, and more.

## Tech Stack

- Python 3.10
- FastAPI
- MongoDB (pymongo)

## Installation

1. Clone the repository:

git clone <repository-url>


2. Install the dependencies:

pip install fastapi pymongo uvicorn


3. Start the FastAPI application:

python main.py

The application will be accessible at http://localhost:8000.

## API Endpoints

- **GET /products**: Retrieve all available products in the system.
- **POST /orders**: Create a new order.
- **GET /orders**: Fetch all orders from the system (supports pagination with `limit` and `offset` parameters).
- **GET /orders/{order_id}**: Fetch a single order by its ID.
- **PUT /products/{product_id}**: Update the available quantity for a product.

## Database

The application uses MongoDB as the database to store products and orders. The database connection details can be configured in `main.py`. By default, the application connects to a local MongoDB instance on the default port (27017).

The MongoDB collections used in the application are:
- **products**: Stores information about the available products.
- **orders**: Stores information about the placed orders.

## Structure

- `main.py`: Contains the main FastAPI application, API endpoints, and MongoDB integration. Defines the data models using Pydantic for products, orders, items, and addresses.

Feel free to explore and modify the code to meet your requirements. If you have any questions, please reach out.

