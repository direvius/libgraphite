from setuptools import setup, find_packages
import sys, os

version = '0.1.3'

setup(name='libgraphite',
      version=version,
      description="Graphite querying library",
      long_description="""\
A Python library for querying metrics from Graphite into Pandas DataFrames
""",
      classifiers=['Topic :: Software Development :: Libraries', 'Topic :: Scientific/Engineering :: Information Analysis', ], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Alexey Lavrenuke (load testing)',
      author_email='direvius@yandex-team.ru',
      url='https://github.com/direvius/libgraphite',
      license='LGPLv3',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          "pandas >= 0.13.1",
          "numpy",
          "requests",
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
