from setuptools import setup, find_packages
import sys, os

version = '0.1.3'

setup(name='libgraphite',
      version=version,
      description="Graphite client",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='',
      author='Alexey Lavrenuke (load testing)',
      author_email='direvius@yandex-team.ru',
      url='',
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
