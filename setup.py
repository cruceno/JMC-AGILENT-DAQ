'''
Created on 21 abr. 2017

@author: Javier M. Cruceño

A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
'''

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path
from future.types.newint import long

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup (
    name='pyagilentdaq',
    version='1.0',
    description='Python application for control and data adquisition with Agilent\'s multimeters',
    long_description=long_description,
    url='https://github.com/cruceno/JMC-AGILENT-DAQ',
    author='Javier M.Cruceño',
    author_email="cruceno@ifir-conicet.gov.ar",
    licence='GNU',
    classifiers=[
        # Operating system supported
        'Operating System :: Microsoft :: Windows :: Windows XP',
        'Operating System :: Microsoft :: Windows :: Windows 10',
        'Operating System :: Microsoft :: Windows :: Windows 7',
        'Operating System :: Microsoft :: Windows :: Windows 8',
        'Operating System :: Microsoft :: Windows :: Windows 8.1',
        
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Science/Research',
        'Topic :: Scientific/Engineering :: Physics',
        'Topic :: Scientific/Engineering :: Visualization',
        'Topic :: Utilities',
        
        # Pick your license as you wish (should match "license" above)
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.

        'Programming Language :: Python :: 3.4',
        'Natural Language :: English',
        ]
    
    
    )
    