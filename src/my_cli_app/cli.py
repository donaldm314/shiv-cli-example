import click
from .main import main as run_main


@click.command()
@click.argument('name')
def main(name):
    """A simple CLI."""
    run_main([name])


if __name__ == '__main__':
    main()
