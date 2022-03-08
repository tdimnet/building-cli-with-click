import click
import os


@click.command(help="Launch on web server")
@click.option("--kind", type=click.Choice(["dev", "prod"]), required=True,
        help="Launch a dev or prod server")
def serve(kind):
    if kind == "dev":
        os.system("flask run --host=0.0.0.0 --port=5000")
    else:
        print('=====')
        print(kind)
        print('=====')

