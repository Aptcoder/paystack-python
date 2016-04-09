"""
A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

from setuptools import setup, find_packages

from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))


# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='paystackapi',
    version='1.2.4',
    description='A python library to consume Paystack API',
    long_description=long_description,
    url='https://github.com/andela-sjames/paystack-python',

    # Author details
    author='Samuel James and Issa Jubril',
    author_email='andela-sjames@andela.com',

    license='MIT',

    keywords='paystack python library',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ],

    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    install_requires=['requests'],

    extras_require={
        'test': ['coverage'],
    },
)
