import click


@click.command(help="Display greetings")
@click.option("--count", default=1, help="Number of greetings.")
@click.option("--name", required=True, help="The person to greet")
def hello(count, name):
    for x in range(count):
        click.echo(f"Hello {name}!")


if __name__ == "__main__":
    hello()

