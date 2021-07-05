import time

import click

from word_squares.indexer.dictionary_dawg_indexer import DictionaryDAWGIndexer
from word_squares.solver.solver_service import SolverService


@click.group()
def cli():
    """
    Cli entry point
    """
    pass


@cli.command()
@click.option("-f", "--filename", type=click.Path(exists=True), prompt=True)
def index_data(filename):
    """
    Entry point to index data functionality
    :param filename: the dictionary file to index
    """
    click.echo("Indexing data")
    DictionaryDAWGIndexer.index_from_file(filename)


@cli.command()
@click.argument("dimension", type=int)
@click.argument("letters")
def solve(dimension: int, letters: str):
    """
    Entry point to the word square puzzle solver functionality
    :param dimension: the length of the words / sides of the square
    :param letters: the available letters to fit to the square
    """

    click.echo(
        "Solving square of dimension {0} with provided letters of {1}".format(
            dimension, letters
        )
    )
    start = time.time()
    solver = SolverService()
    result = solver.generate_word_square(dimension, letters)
    if result is not False:
        end = time.time()
        print(f"Successfully generated word square in {round(end - start, 2)} seconds")

        for row in result:
            print("".join(row))

    else:
        print("Unable to find solution")


if __name__ == "__main__":
    cli()
