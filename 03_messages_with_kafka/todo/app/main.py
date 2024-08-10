from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
from todo.app import settings
from aiokafka import AIOKafkaProducer, AIOKafkaConsumer
from confluent_kafka.admin import AdminClient, NewTopic

app = FastAPI()

# Order model
class Order(BaseModel):
    id: int
    customer_name: str
    item: str
    quantity: int
    price: float

# In-memory orders storage
orders = []

# Create an order
@app.post("/orders/", response_model=Order)
async def create_order(order: Order):
    producer=AIOKafkaProducer(settings.BOOTSTRAP_SERVER)
    await producer.start()
    orders.append(order)
    return order

# Get all orders
@app.get("/orders/", response_model=List[Order])
def read_orders():
    return orders

# Get a single order by ID
@app.get("/orders/{order_id}", response_model=Order)
def read_order(order_id: int):
    for order in orders:
        if order.id == order_id:
            return order
    raise HTTPException(status_code=404, detail="Order not found")

# Update an order
@app.put("/orders/{order_id}", response_model=Order)
def update_order(order_id: int, order_update: Order):
    for index, order in enumerate(orders):
        if order.id == order_id:
            orders[index] = order_update
            return order_update
    raise HTTPException(status_code=404, detail="Order not found")

# Delete an order
@app.delete("/orders/{order_id}", response_model=Order)
def delete_order(order_id: int):
    for index, order in enumerate(orders):
        if order.id == order_id:
            return orders.pop(index)
    raise HTTPException(status_code=404, detail="Order not found")

