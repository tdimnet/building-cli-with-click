import click
from sqlalchemy.sql import text

from store_inventory.models import Base, engine
from store_inventory.csv import (
    add_order_status_to_db,
    add_products_csv_to_database,
    add_orders_to_db
)


@click.group(help="Generate data and also create and detele the database")
def database():
    pass


@click.command(help="Create a database and tables")
def create():
    click.echo("Creating the database and the tables")
    Base.metadata.create_all(engine)


@click.command(help="Read the CSV file and populate data into the Database")
def populate():
    click.echo("Get data from the CSV and populate the Database")

    #click.echo("Adding the status of orders")
    #add_order_status_to_db()

    #click.echo("Adding products")
    #add_products_csv_to_database()

    click.echo("Adding orders")
    add_orders_to_db()


@click.command(help="Clean duplicate rows within a table")
@click.option("--name",
        prompt="Name of the table", 
        help="The name of the table you want to clean",
        required=True)
def clean_table(name):
    click.echo(f"Cleaning the {name} table")

    try:
        with engine.connect() as con:
            if not engine.dialect.has_table(con, name):
                raise ValueError(f"The table {name} was not found")

            # Add comment
            statement = text("DELETE t1 FROM product t1 INNER JOIN product t2 WHERE t1.id < t2.id AND t1.name = t2.name;")
            click.echo(f"{name} table cleaned")
    except Exception as err:
        click.echo("Something went wrong when cleaning the table")


@click.command(help="Drop the database including all the database inside")
@click.option("--force", is_flag=True)
def drop(force):
    if force:
        click.echo("Drop the database")
        Base.metadata.drop_all(engine)


database.add_command(create)
database.add_command(drop)
database.add_command(clean_table)
database.add_command(populate)

