import click
from datetime import datetime


from store_inventory.models import session, Product


@click.group(help="Get, update or delete a product")
def product():
    pass


@click.command(help="Retrieve and print a product")
@click.option("--id", required=True, type=int)
def get(id):
    click.echo(f"Retrieve the product with the ID {id}")

    product = session.query(Product).filter(Product.id == id).one_or_none()
    
    if product == None:
        click.echo(f"The product with the ID {id} doesn't exist in the Database")
    else:
        click.echo(product)


@click.command()
def update():
    my_file = open("/app/notes.txt", "a")
    my_file.write(f"\nAccessed on {str(datetime.now())}")


product.add_command(get)
product.add_command(update)

