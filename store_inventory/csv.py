import csv


def add_csv():
    with open('/app/store_inventory/inventory/inventory.csv') as csv_file:
        products_data = list(csv.DictReader(csv_file))

        for product in products_data:
            name = product["product_name"]
            price = product["product_price"]
            quantity = product["product_quantity"]
            date = product["date_updated"]


            print("========")
            print(name)
            print(price)
            print(quantity)
            print(date)
            print("========")

