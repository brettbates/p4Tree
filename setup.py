import os
import sys
from setuptools import setup
from p4treelib import __version__

setup(
    name = "p4treelib",
    version = __version__,
    url = 'https://github.com/brettbates/p4treelib',
    author = 'brettbates',
    author_email = 'mogwairn@gmail.com',
    description = 'pyTree with added access level and option to differentiate node typed between a user and a path. Based completely off of: https://github.com/caesar0301/pyTree, much of the credit goes to the creator caesar0301',
    long_description='''This is a simple tree data structure implementation in python.''',
    license = "LICENSE",
    packages = ['p4treelib', 'tests'],
    keywords = ['data structure', 'tree', 'tools'],
    classifiers = [
        'Development Status :: 4 - Beta',
        'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: Freely Distributable',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 2.6',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3.2',
            'Topic :: Software Development :: Libraries :: Python Modules',
   ],
)
