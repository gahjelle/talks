import sys


class DebugFinder:
    """List all modules as they are imported"""

    @classmethod
    def find_spec(cls, name, path, target=None):
        """Print name of module, don't load anything"""
        print(f"Importing {name!r}")
        return None


# Insert DebugFinder before any other finder
sys.meta_path.insert(0, DebugFinder)
