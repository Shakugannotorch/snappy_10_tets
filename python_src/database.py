from __future__ import print_function
import sys, sqlite3, re, os, random
import snappy_manifolds

# This module uses sqlite3 databases with multiple tables.
# The path to the database file is specified at the module level.
from .sqlite_files import __path__ as manifolds_paths
manifolds_path = manifolds_paths[0]
database_path = os.path.join(manifolds_path, '10_tet.sqlite')

split_filling_info = re.compile(r'(.*?)((?:\([0-9 .+-]+,[0-9 .+-]+\))*$)')

def get_tables(ManifoldTable):
    """
    Functions such as this one are meant to be called in the
    __init__.py module in snappy proper.  To avoid circular imports,
    it takes as argument the class ManifoldTable from database.py in
    snappy. From there, it builds all of the Manifold tables from the
    sqlite databases manifolds.sqlite and more_manifolds.sqlite in
    manifolds_src, and returns them all as a list.
    """

    class TenTetCuspedCensus(ManifoldTable):
        """ 
        Iterator for all knots up to 14 or 15 crossings (see below for
        which) and links up to 14 crossings as tabulated by Jim Hoste
        and Morwen Thistlethwaite.  In addition to the filter
        arguments supported by all ManifoldTables, this iterator
        provides alternating=<True/False>;
        knots_vs_links=<'knots'/'links'>; and crossings=N. These allow
        iterations only through alternating or non-alternating links
        with 1 or more than 1 component and a specified crossing
        number.
        """

        _regex = re.compile(r'([msvt])([0-9]+)$|o9_\d\d\d\d\d$|o10_\d\d\d\d\d\d$')
        
        def __init__(self, **kwargs):
            return ManifoldTable.__init__(self,
                                         table='hyperbolic_cusped_census_view',
                                         db_path=database_path,
                                         **kwargs)

        def _configure(self, **kwargs):
            """
            Process the ManifoldTable filter arguments and then add
            the ones which are specific to links.
            """
            ManifoldTable._configure(self, **kwargs)

    return [TenTetCuspedCensus()]


def connect_to_db(db_path):
    """
    Open the given sqlite database, ideally in read-only mode.
    """
    if sys.version_info >= (3,4):
        uri = 'file:' + db_path + '?mode=ro'
        return sqlite3.connect(uri, uri=True)
    elif sys.platform.startswith('win'):
        try:
            import apsw
            return apsw.Connection(db_path, flags=apsw.SQLITE_OPEN_READONLY)
        except ImportError:
            return sqlite3.connect(db_path)
    else:
        return sqlite3.connect(db_path)
