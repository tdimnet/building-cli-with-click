import csv

from store_inventory.models import session, Product, ProductState
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
            product_state_id = PRODUCT_INITIAL_STATE

            new_product = Product(
                name=name,
                price=price,
                quantity=quantity,
                created_at=created_at,
                updated_at=updated_at,
                product_state_id=product_state_id
            )
            session.add(new_product)

        session.commit()


def add_product_states_csv_to_db():
    with open('/app/store_inventory/inventory/product_states.csv') as csv_file:
        product_states = list(csv.DictReader(csv_file))

        for state in product_states:
            name = state["state_name"]

            new_state = ProductState(
                name=name
            )

            session.add(new_state)

        session.commit()

