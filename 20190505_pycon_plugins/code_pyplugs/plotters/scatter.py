"""Plot a scatter plot"""

# Third party imports
import pyplugs
import seaborn as sns


@pyplugs.register
def scatter(ax, data):
    """Plot a scatter plot"""
    x, y, *_ = data.columns  # First two columns
    sns.scatterplot(data[x], data[y], ax=ax)
