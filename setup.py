from os.path import abspath, dirname, join

from setuptools import setup

from pykka_injector import __version__

PROJECT_ROOT = abspath(dirname(__file__))

long_description = open(join(PROJECT_ROOT, 'README.rst')).read()
description = 'Pykka/Injector integration module'

setup(
    name='pykka_injector',
    url='http://github.com/jstasiak/pykka_injector',
    download_url='http://pypi.python.org/pypi/pykka_injector',
    version=__version__,
    description=description,
    long_description=long_description,
    license='MIT',
    platforms=['any'],
    py_modules=['pykka_injector'],
    author='Jakub Stasiak',
    author_email='jakub@stasiak.at',
    install_requires=[
        'setuptools >= 0.6b1',
        'pykka',
        'injector',
    ],
)
