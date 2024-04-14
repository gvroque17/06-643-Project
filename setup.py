"""Setup for the package."""

from setuptools import setup

setup(name='ReferencedWorkSort',
      version='0.0.1',
      description='Sorts referenced work by first author',
      maintainer='Graciela Vargas Roque',
      maintainer_email='gvargasr@andrew.cmu.edu',
      license='MIT',
      packages=['ReferencedWorkSort'],
      entry_points={'console_scripts': ['referenced_work_sort=ReferencedWorkSort.utils:referenced_work_sort']},  
      scripts=[],
      long_description='''For a paper OID, lists referenced work grouped by author
=========================''')
