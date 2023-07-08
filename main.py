from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from pymongo import MongoClient

app = FastAPI()

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["ecommerce"]


# define the MongoDB collection names

PRODUCTS_COLLECTION = "products"
ORDERS_COLLECTION = "orders"


#define the data models for the product, order, and user address using Pydantic: 

class Product(BaseModel):
    name: str
    price: float
    quantity: int


class Item(BaseModel):
    product_id: str
    bought_quantity: int


class Address(BaseModel):
    city: str
    country: str
    zip_code: str


class Order(BaseModel):
    timestamp: str
    items: List[Item]
    total_amount: float
    address: Address

#Create the API endpoints for listing products 
@app.get("/products")
def get_products():
    products = list(db[PRODUCTS_COLLECTION].find())
    return products

#Create the API endpoints for creating an order

@app.post("/orders")
def create_order(order: Order):
    order_dict = order.dict()
    order_id = db[ORDERS_COLLECTION].insert_one(order_dict).inserted_id
    order_dict["_id"] = str(order_id)
    return order_dict
 #Create the API endpoints for fetching all orders,

@app.get("/orders")
def get_orders(limit: int = 10, offset: int = 0):
    orders = list(db[ORDERS_COLLECTION].find().skip(offset).limit(limit))
    return orders

#Create the API endpoints for fetching a single order
@app.get("/orders/{order_id}")
def get_order(order_id: str):
    order = db[ORDERS_COLLECTION].find_one({"_id": order_id})
    if order:
        return order
    else:
        raise HTTPException(status_code=404, detail="Order not found")

#Create the API endpoints for and updating a product:

@app.put("/products/{product_id}")
def update_product(product_id: str, quantity: int):
    result = db[PRODUCTS_COLLECTION].update_one(
        {"_id": product_id},
        {"$set": {"quantity": quantity}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="Product not found")
    else:
        return {"message": "Product updated"}
    
# start the application

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
