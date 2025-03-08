# 'setup.py' will contain local package installation code. This file is used to install the package locally.

from setuptools import find_packages, setup

setup(
    name = 'wasteDetection',
    version = '0.0.0',
    author = 'Kunal Mishra',
    author_email = 'mishrakunal065@gmail.com',
    packages = find_packages(), # It will find all the constructor('__init__.py') file in every folder and subfolder and install that folder as a local package so that I can import them in other files
    install_requires = []
)
