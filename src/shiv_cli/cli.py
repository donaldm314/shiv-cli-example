import click
from .main import main as run_main

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])


@click.command(context_settings=CONTEXT_SETTINGS)
@click.argument('name')
def main(name):
    """A simple CLI."""
    run_main([name])


if __name__ == '__main__':
    main()
