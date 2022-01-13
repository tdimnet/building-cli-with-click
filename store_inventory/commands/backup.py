import click


@click.group()
def backup():
    pass


@click.command()
@click.option("-d", "--dump", is_flag=True)
def generate(dump):
    click.echo("Generate Database backup")
    click.echo(dump)


@click.command()
def delete():
    click.echo("Delete Database backup")


backup.add_command(generate)
backup.add_command(delete)

