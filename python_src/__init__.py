__version__ = '1.01'

def version():
    return __version__

import sys
from .database import get_tables

try:
    import snappy
    table_dict = snappy.database.add_tables_from_package('snappy_10_tets', False)
    for name, table in table_dict.items():
        setattr(snappy, name, table)
        if name not in snappy.database_objects:
            snappy.database_objects.append(name)
except ImportError:
    raise RuntimeError('Error happened when loading 10 tet census data to SnapPy')