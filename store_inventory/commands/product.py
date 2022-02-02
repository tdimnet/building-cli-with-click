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
    click.echo("Let's update a product")
    my_file = open("/app/notes.txt", "a")
    my_file.write(f"\nAccessed on {str(datetime.now())}\n")


@click.command()
def update_product():
    click.echo("Let's update a product")

    product = session.query(Product).filter(Product.product_state_id ==
            2).limit(1).one_or_none()

    if product == None:
        click.echo("Not found")
    else:
        product.product_state_id = 3
        session.commit()


product.add_command(get)
product.add_command(update)
product.add_command(update_product)

