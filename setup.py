"""Setup for the package."""

from setuptools import setup

setup(name='RefWorkSortPkg',
      version='0.0.1',
      description='Sorts referenced work by first author',
      maintainer='Graciela Vargas Roque',
      maintainer_email='gvargasr@andrew.cmu.edu',
      license='MIT',
      packages=['RefWorkSortPkg'],
      entry_points={
          'console_scripts': [
              'referenced_work_sort=RefWorkSortPkg.utils:referenced_work_sort']
      },
      scripts=[],
      long_description='''For a paper OID, lists referenced work grouped by author
=========================''')
