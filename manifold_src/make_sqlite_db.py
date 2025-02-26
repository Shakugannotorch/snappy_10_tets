import os, sys, time
import sqlite3
import binascii
import re
import csv

"""
This file contains the functions used to pull the data
from the Manifold censuses in csv format to build sqlite
databases for use by snappy. The first line of the csv
names the columns.
"""

csv_dir = 'original_manifold_sources'

schema_types = {
    'id': 'int',
    'name': 'text',
    'cusps': 'int',
    'betti': 'int',
    'torsion': 'text',
    'volume': 'real',
    'chernsimons': 'real',
    'tets': 'int', 
    'hash': 'text',
    'triangulation': 'text',
}


def make_table(connection, tablename, csv_files, name_index=True):
    """
    Given a csv of manifolds data and a connection to a sqlite database,
    insert the data into a new table. If the csv file is in a subdirectory
    of the csv directory csv_dir, it is given by sub_dir.
    """
    # Get the column names from the first csv file
    first_csv_file = open(os.path.join(csv_dir, csv_files[0]), 'r')
    csv_reader = csv.reader(first_csv_file)
    columns = next(csv_reader)
    
    schema = "CREATE TABLE %s (id integer primary key" % tablename
    for column in columns[1:]: #first column is always id
        schema += ",%s %s" % (column,schema_types[column])
    schema += ")"
    print('creating ' + tablename)
    connection.execute(schema)
    connection.commit()
    
    insert_query = "insert into %s ("%tablename
    for column in columns:
        insert_query += "%s, " %column
    insert_query = insert_query[:-2] #one comma too many
    insert_query += ') values ('
    for column in columns:
        if schema_types[column] == 'text':
            insert_query += "'%s', "
        else:
            insert_query += "%s, "
    insert_query = insert_query[:-2] #one comma too many
    insert_query += ')'

    for csv_file in csv_files:
        csv_reader = csv.reader(open(os.path.join(csv_dir, csv_file)))
        assert columns == next(csv_reader)
        for row in csv_reader:
            data_list = row
            for i,data in enumerate(data_list): #chernsimons is None sometimes
                if data == 'None':
                    data_list[i] = 'Null'
            connection.execute(insert_query%tuple(data_list))

    # We need to index columns that will be queried frequently for speed.

    indices = ['hash', 'volume']
    if name_index:
        indices += ['name']
    #print('Indices: {}'.format(indices))
    for column in indices:
        connection.execute(
            'create index %s_by_%s on %s (%s)'%
            (tablename, column, tablename, column))
    connection.commit()
            
def is_stale(dbfile, sourceinfo):
    if not os.path.exists(dbfile):
        return True
    dbmodtime = os.path.getmtime(dbfile)
    for table in sourceinfo:
        for csv_file in sourceinfo[table]['csv_files']:
            csv_path = os.path.join(csv_dir, csv_file)
            if os.path.getmtime(csv_path) > dbmodtime:
                return True
    return False
    
if __name__ == '__main__':
    manifold_db = '10_tet.sqlite'
    manifold_data = {'hyperbolic_cusped_census': {'csv_files': ['orientable_cusped_census.csv',
                                                'orientable_cusped_census_10.csv']}}
    
    if is_stale(manifold_db, manifold_data):
        if os.path.exists(manifold_db):
            os.remove(manifold_db)
        with sqlite3.connect(manifold_db) as connection:
            for tablename, args in manifold_data.items():
                make_table(connection, tablename, **args)
            connection.execute(" create view HT_links_view as select * from HT_links")

