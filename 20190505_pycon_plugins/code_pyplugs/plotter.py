"""Plotter - Simple plotting application
"""

# Standard library imports
import pathlib

# Third party imports
import click
import matplotlib.pyplot as plt

# Plotter imports
import plotters
import readers


def read_data(file_path):
    """Read data from a file, return a Pandas DataFrame"""
    reader = file_path.suffix.lstrip(".")
    return readers.read(reader, file_path=file_path)


def create_plot(data, plotter):
    """Plot a Pandas DataFrame"""
    fig, ax = plt.subplots()
    for group, data_group in data:
        plotters.plot(plotter, ax=ax, data=data_group)
    plt.show()


@click.command()
@click.argument("file_path", type=click.Path(exists=True))
@click.option("-c", "--cols", help="Columns to plot")
@click.option(
    "-k", "--kind", default="line", help=f"Kind of plot [{', '.join(plotters.names())}]"
)
@click.option("-g", "--groupby", help="Column to group by")
def main(file_path, cols, kind, groupby):
    """Read data from file and make a plot"""
    file_path = pathlib.Path(file_path)

    data = read_data(file_path)
    if cols:
        cols_list = cols.split(",")
        if groupby:
            cols_list += [groupby]
        data = data[cols_list]

    if groupby:
        data = data.groupby(groupby)
    else:
        data = ((0, data),)

    create_plot(data, plotter=kind)


if __name__ == "__main__":
    main()
