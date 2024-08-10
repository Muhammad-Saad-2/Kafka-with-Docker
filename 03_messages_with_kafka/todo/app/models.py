from sqlalchemy import Column, Integer, String, Float 
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Order(Base):
    __tablename__ = "orders"
    id = Column(Integer, primary_key=True, index=True)
    customer_name=Column(String, index=True)
    item= Column(String, index=True)
    quantity= Integer(String, index=True)
    price= Column(Float, index=True)
