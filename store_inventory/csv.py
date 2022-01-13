import csv

from store_inventory.models import session, Product
from store_inventory.utils.date import clean_date
from store_inventory.utils.price import clean_price


def add_csv_to_database():
    with open('/app/store_inventory/inventory/inventory.csv') as csv_file:
        products_data = list(csv.DictReader(csv_file))

        for product in products_data:
            name = product["product_name"]
            price = clean_price(product["product_price"])
            quantity = int(product["product_quantity"])
            date = clean_date(product["date_updated"])

            new_product = Product(
                name=name,
                price=price,
                quantity=quantity,
                created_at=date
            )
            session.add(new_product)

        session.commit()

