from sqlalchemy import (
    Column,
    Date,
    ForeignKey,
    Integer,
    String,
    create_engine
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

    product_state_id = Column(Integer, ForeignKey('product_states.id'))
    product_state = relationship("ProductState")

    def __repr__(self) -> str:
        return f"({self.id}) - Product name: {self.name}"


class ProductState(Base):
    __tablename__ = "product_states"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(255))

    def __repr__(self):
        return f"({self.id} - State Name: {self.name})"


class ProductQuantity(Base):
    __tablename__ = "product_quantities"

    id = Column(Integer, primary_key=True)
    quantity = Column("quantity", Integer)


class Order(Base):
    __tablename__ = "orders"

    id = Column(Integer, primary_key=True)
    products = Column("products", String(255))
    created_at = Column("created_at", Date)
    updated_at = Column("updated_at", Date)

