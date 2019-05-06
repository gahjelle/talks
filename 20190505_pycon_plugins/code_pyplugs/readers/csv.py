"""Reader for CSV files"""

# Third party imports
import pandas as pd
import pyplugs


@pyplugs.register
def csv(file_path):
    """Read a CSV file, store to Pandas DataFrame"""
    return pd.read_csv(file_path)
