from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    create_engine,
    Table
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('mysql+pymysql://dev:example@db/inventory_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(255))
    price = Column("price", Integer)
    quantity = Column("quantity", Integer)
    created_at = Column("created_at", Date)
    updated_at = Column("updated_at", Date)

    def __repr__(self) -> str:
        return f"({self.id}) - Product name: {self.name}"


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    created_at = Column("created_at", Date)
    updated_at = Column("updated_at", Date)

    products = relationship("ProductsOrder") 

    order_status_id = Column(Integer, ForeignKey("order_status.id"))
    order_status = relationship("OrderStatus")


class ProductsOrder(Base):
    __tablename__ = "products_order"

    id = Column("id", Integer, primary_key=True)
    quantity = Column("quantity", Integer)
    order_id = Column("order_id", ForeignKey("orders.id"))
    product_id = Column("product_id", ForeignKey("products.id"))


class OrderStatus(Base):
    __tablename__ = "order_status"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(255))

    def __repr__(self):
        return f"({self.id} - State Name: {self.name})"

