"""Plot linear regression plot"""

# Third party imports
import pyplugs
import seaborn as sns


@pyplugs.register
def lin_reg(ax, data):
    """Plot a linear regression"""
    x, y, *_ = data.columns  # First two columns
    sns.regplot(x, y, ax=ax, data=data)
