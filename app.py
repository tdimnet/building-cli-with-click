import click

from store_inventory.commands.backup import backup
from store_inventory.commands.database import database
from store_inventory.commands.server import serve
from store_inventory.commands.product import product
from store_inventory.commands.cron import cron


@click.group()
def cli():
    pass


cli.add_command(database)
cli.add_command(backup)
cli.add_command(serve)
cli.add_command(product)
cli.add_command(cron)


if __name__ == "__main__":
    cli()

