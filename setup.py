import re, sys, subprocess, os, shutil, glob, sysconfig
from setuptools import setup, Command
from setuptools.command.build_py import build_py

sqlite_files = ['10_tet.sqlite']

setup(
    packages = ['snappy_10_tets', 'snappy_10_tets/sqlite_files'],
    package_dir = {'snappy_10_tets':'python_src',
                   'snappy_10_tets/sqlite_files':'manifold_src'},
    package_data = {'snappy_10_tets/sqlite_files': sqlite_files},
    ext_modules = [],
    zip_safe = False
)