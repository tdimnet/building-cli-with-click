import click


from store_inventory.models import session, Product


@click.group()
def product():
    pass


@click.command()
@click.option("--id", required=True, type=int)
def get(id):
    click.echo(f"Retrieve the product with the ID {id}")

    product = session.query(Product).filter(Product.id == id).one_or_none()
    
    if product == None:
        click.echo(f"The product with the ID {id} doesn't exist in the Database")
    else:
        click.echo(product)


product.add_command(get)

