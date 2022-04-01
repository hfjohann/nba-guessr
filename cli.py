import click
from mlib import get_closest


@click.command()
@click.option("-p", "--points", prompt="Enter PPG", default=27, help="Points per game")
@click.option(
    "-r", "--rebounds", prompt="Enter RPG", default=7, help="Rebounds per game"
)
@click.option("-a", "--assists", prompt="Enter APG", default=7, help="Points per game")
def getclosestplayers(points, rebounds, assists):
    click.echo(get_closest(points, rebounds, assists))


if __name__ == "__main__":
    getclosestplayers()
