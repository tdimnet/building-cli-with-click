import click

from store_inventory.models import Base, engine
from store_inventory.csv import add_csv


@click.group()
def database():
    pass


@click.command()
def create():
    click.echo("Create the Database")
    Base.metadata.create_all(engine)


@click.command()
def populate():
    click.echo("Get data from the CSV and populate the Database")
    add_csv()


@click.command()
def drop():
    click.echo("Drop the Database")
    Base.metadata.drop_all(engine)


database.add_command(create)
database.add_command(drop)
database.add_command(populate)

