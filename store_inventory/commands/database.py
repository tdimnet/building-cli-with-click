import click

from store_inventory.models import Base, engine
from store_inventory.csv import add_csv_to_database


@click.group(help="Generate data and also create and detele the database")
def database():
    pass


@click.command(help="Create a databae and tables")
def create():
    click.echo("Creating the database and the tables")
    Base.metadata.create_all(engine)


@click.command(help="Read the CSV file and populate data into the Database")
def populate():
    click.echo("Get data from the CSV and populate the Database")
    add_csv_to_database()


@click.command(help="Drop the database including all the database inside")
@click.option("--force", is_flag=True)
def drop(force):
    if force:
        click.echo("Drop the database")
        Base.metadata.drop_all(engine)


database.add_command(create)
database.add_command(drop)
database.add_command(populate)

