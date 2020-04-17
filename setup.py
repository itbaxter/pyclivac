import sys
from setuptools import find_packages, setup


DISTNAME = 'pyclivac'
VERSION = 0.0
LICENSE = 'MIT'
AUTHOR = 'Deanna Nash & Tessa Montini'
AUTHOR_EMAIL = 'dlnash@ucsb.edu'
CLASSIFIERS = [
         "Programming Language :: Python :: 3",
         "Operating System :: OS Independent",
         ]
SETUP_REQUIRES = find_packages

DESCRIPTION = ""
LONG_DESCRIPTION = """
A series of programs designed for UCSB Climate Variability and Changes (CLIVAC) research group developed by Tessa Montini and Deanna Nash.
"""

setup(name=DISTNAME,
      version=VERSION,
      license=LICENSE,
      author=AUTHOR,
      author_email=AUTHOR_EMAIL,
      classifiers=CLASSIFIERS,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      packages=find_packages())
