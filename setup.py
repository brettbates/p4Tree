import os
import sys
from setuptools import setup
from treelib import __version__

setup(
    name = "p4treelib",
    version = __version__,
    url = 'https://github.com/caesar0301/pyTree',
    author = 'caesar0301',
    author_email = 'chenxm35@gmail.com',
    description = 'pyTree with added access level. Based completely off of: https://github.com/caesar0301/pyTree, all credit goes to the creator',
    long_description='''This is a simple tree data structure implementation in python.''',
    license = "LICENSE",
    packages = ['treelib'],
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
