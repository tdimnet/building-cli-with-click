from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://dev:example@db/inventory_db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    name = Column("name", String(255))
    price = Column("price", Integer)
    quantity = Column("quantity", Integer)
    date = Column("created_at", Date)
    

    def __repr__(self) -> str:
        return f"({self.id}) - First Name: {self.first_name}, Last Name: {self.last_name}"


