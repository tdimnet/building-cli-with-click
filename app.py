import click
import os

from store_inventory.commands.backup import backup
from store_inventory.commands.database import database
from store_inventory.commands.server import serve
from store_inventory.commands.product import product


@click.group()
def cli():
    pass


cli.add_command(database)
cli.add_command(backup)
cli.add_command(serve)
cli.add_command(product)


if __name__ == "__main__":
    cli()

