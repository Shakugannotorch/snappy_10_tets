__version__ = '1.0'

def version():
    return __version__

import sys
from .database import get_tables

try:
    import snappy
    table_dict = snappy.database.add_tables_from_package('ten_tet_census', False)
    for name, table in table_dict.items():
        setattr(snappy, name, table)
        if name not in snappy.database_objects:
            snappy.database_objects.append(name)
except ImportError:
    print('er')