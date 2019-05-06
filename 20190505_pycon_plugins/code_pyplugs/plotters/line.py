"""Plot a line plot"""

# Third party imports
import pyplugs


@pyplugs.register
def line(ax, data):
    """Plot a line plot"""
    data.plot(ax=ax)
