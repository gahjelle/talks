"""Simple plotting of your datafiles"""

# Standard library imports
import pathlib

# Third party imports
import click
import matplotlib.pyplot as plt

# Plotter imports
import readers


def read_data(file_path):
    """Read data, return Pandas DataFrame"""
    format = file_path.suffix.lstrip(".")
    return readers.read(format, file_path=file_path)


def create_plot(data):
    """Plot a Pandas dataframe"""
    data.plot()
    plt.show()


@click.command()
@click.argument("file_path")
def main(file_path):
    """Read data and create a simple plot"""
    file_path = pathlib.Path(file_path)

    data = read_data(file_path)
    create_plot(data)


if __name__ == "__main__":
    main()
