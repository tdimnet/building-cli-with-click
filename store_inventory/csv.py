import csv

from store_inventory.models import (
    Product,
    OrderStatus,
    Order,
    session,
    ProductsOrder
)
from store_inventory.utils.date import (
    clean_date,
    generate_date
)
from store_inventory.utils.price import clean_price


ORDER_CONFIRMED_STATUS = 2


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
                name=status_name,
                created_at=generate_date(),
                updated_at=generate_date()
            )

            session.add(new_order_status)

        session.commit()


def add_orders_to_db():
    print("====")

    created_at = clean_date("03/02/2021")
    updated_at = clean_date("03/02/2021")

    new_order = Order(
        order_status_id=ORDER_CONFIRMED_STATUS,
        created_at=created_at,
        updated_at=updated_at
    )

    session.add(new_order)
    session.commit()

    print(new_order.products)
    
    new_product_order = ProductsOrder(
        quantity=1,
        order_id=new_order.id,
        product_id=1
    )

    new_order.products.append(new_product_order)

    session.commit()

