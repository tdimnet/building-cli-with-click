import click
import os

from store_inventory.csv import add_csv


@click.group()
def cli():
    pass


@click.command()
@click.option('--dev/--prod', default=False)
def serve(dev):
    if dev == True:
        click.echo("Launch dev server")
        os.system("flask run --host=0.0.0.0")
    else:
        click.echo("Lauching prod server")


@click.group()
def backup():
    pass


@click.command()
def read():
    click.echo('Read the CSV backup file')
    add_csv()


@click.command()
@click.option("-d", "--dump", is_flag=True)
def generate(dump):
    click.echo("Generate Database backup")
    click.echo(dump)


@click.command()
def delete():
    click.echo("Delete Database backup")


backup.add_command(read)
backup.add_command(generate)
backup.add_command(delete)

cli.add_command(backup)
cli.add_command(serve)



if __name__ == "__main__":
    cli()

