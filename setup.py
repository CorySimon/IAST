from __future__ import absolute_import
from __future__ import print_function
import sys
from setuptools import setup

if sys.version_info[0] != 3:
    print("pyIAST now requires Python 3.")
    sys.exit(1)

setup(
    name='pyiast',
    version='1.4.2',
    description='Ideal Adsorbed Solution Theory',
    url='https://github.com/CorySimon/pyIAST',
    download_url='https://github.com/CorySimon/pyIAST/tarball/master',
    install_requires=['numpy', 'scipy', 'pandas', 'matplotlib'],
    extras_require={'pre-commit': [
        "pre-commit==1.14.4",
        "yapf==0.26.0",
    ]},
    keywords='chemistry isotherm iast',
    author='Cory M. Simon',
    author_email='CoryMSimon@gmail.com',
    license='MIT',
    packages=['pyiast'],
    zip_safe=False)
