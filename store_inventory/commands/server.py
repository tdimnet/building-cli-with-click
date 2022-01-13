import click
import os


@click.command()
@click.option('--dev/--prod', default=False)
def serve(dev):
    if dev == True:
        click.echo("Launch dev server")
        os.system("flask run --host=0.0.0.0")
    else:
        click.echo("Lauching prod server")

