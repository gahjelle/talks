"""Reader for JSON files"""

# Standard library imports
import json as jsonlib

# Third party imports
import pandas as pd
import pyplugs


@pyplugs.register
def json(file_path):
    """Read a JSON file, store to Pandas DataFrame"""
    with open(file_path, mode="r") as fid:
        data = jsonlib.load(fid)
    return pd.DataFrame(data)
