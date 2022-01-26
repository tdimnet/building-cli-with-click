import click

from store_inventory.crons import (
    add_product_crons,
    list_crons
)

@click.group()
def cron():
    pass


@click.command()
def products():
    click.echo("Add crons for product")
    add_product_crons()


@click.command()
def list():
    click.echo("Here are the running job")
    list_crons()


cron.add_command(products)
cron.add_command(list)

