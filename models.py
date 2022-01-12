from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+pymysql://dev:example@db/my_database', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()


class Product(Base):
    __tablename__ = "people"

    id = Column(Integer, primary_key=True)
    first_name = Column("first_name", String(255))
    last_name = Column("last_name", String(255))

    def __repr__(self) -> str:
        return f"({self.id}) - First Name: {self.first_name}, Last Name: {self.last_name}"


