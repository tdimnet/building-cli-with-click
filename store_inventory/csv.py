import csv

from store_inventory.models import (
    Product,
    OrderStatus,
    session
)
from store_inventory.utils.date import clean_date
from store_inventory.utils.price import clean_price


PRODUCT_INITIAL_STATE = 1


def add_products_csv_to_database():
    with open('/app/store_inventory/inventory/products.csv') as csv_file:
        products_data = list(csv.DictReader(csv_file))

        for product in products_data:
            name = product["product_name"]
            price = clean_price(product["product_price"])
            quantity = int(product["product_quantity"])
            created_at = clean_date(product["date_updated"])
            updated_at = clean_date(product["date_updated"])

            new_product = Product(
                name=name,
                price=price,
                quantity=quantity,
                created_at=created_at,
                updated_at=updated_at
            )

            session.add(new_product)

        session.commit()


def add_order_status_to_db():
    with open("/app/store_inventory/inventory/order_status.csv") as csv_file:
        order_status = list(csv.DictReader(csv_file))

        for status in order_status:
            status_name = status["status_name"]

            new_order_status = OrderStatus(
                name=status_name
            )

            session.add(new_order_status)

        session.commit()

