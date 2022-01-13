import csv


def add_csv():
    with open('/app/store_inventory/inventory/inventory.csv') as csv_file:
        products_data = list(csv.DictReader(csv_file))

        print('=====')
        print(products_data)
        print('=====')

