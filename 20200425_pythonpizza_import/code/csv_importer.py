import csv
import pathlib
import sys
from importlib.machinery import ModuleSpec


class CsvImporter:
    """Import CSV files as modules"""

    def __init__(self, csv_path):
        """Store path to CSV file"""
        self.csv_path = csv_path

    @classmethod
    def find_spec(cls, fullname, path=None, target=None):
        """Find CSV file in import path"""
        directories = sys.path if path is None else path
        file_name = f"{fullname.rpartition('.')[-1]}.csv"
        for directory in directories:
            csv_path = pathlib.Path(directory) / file_name
            if csv_path.exists():
                return ModuleSpec(fullname, cls(csv_path))

        # No CSV file was found
        return None

    def create_module(self, spec):
        """Return None to use Python's default module creator"""
        return None

    def exec_module(self, module):
        """Read the CSV file and store it as attributes on the module"""
        # Read CSV data and store it as a list of dictionaries
        with self.csv_path.open() as fid:
            rows = csv.DictReader(fid)
            data = list(rows)
            fieldnames = tuple(rows.fieldnames)

        # Create a dictionary for each field
        values = zip(*(row.values() for row in data))
        fields = dict(zip(fieldnames, values))

        # Add the CSV data to the module
        module.__dict__.update(fields)
        module.__dict__["data"] = data
        module.__dict__["fieldnames"] = fieldnames


# Add CsvImporter as the last finder
sys.meta_path.append(CsvImporter)
