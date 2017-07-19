# -*- coding: utf-8 -*-
"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
# To use a consistent encoding
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='a2pcej',
    version='0.2.2a3',
    description='''a2pcej, "convert Alphabet to Phonetic Code in English
                   and Japanease."''',
    long_description=long_description,
    url='https://github.com/kacchan822/a2pcej',
    author='Katsuya SAITO',
    author_email='hello@skatsuya.com',
    license='MIT',
    classifiers=[
                    'Development Status :: 3 - Alpha',
                    'Environment :: Console',
                    'Intended Audience :: Developers',
                    'Intended Audience :: System Administrators',
                    'Intended Audience :: Customer Service',
                    'License :: OSI Approved :: MIT License',
                    'Natural Language :: Japanese',
                    'Natural Language :: English',
                    'Operating System :: POSIX',
                    'Programming Language :: Python',
                    'Programming Language :: Python :: 2',
                    'Programming Language :: Python :: 2.7',
                    'Programming Language :: Python :: 3',
                    'Programming Language :: Python :: 3.5',
                    'Topic :: Software Development',
                    'Topic :: Text Processing',
                    'Topic :: Utilities',
                    ],
    keywords='alphabet, katakana, phonetic code',
    packages=find_packages(exclude=['tests', ]),
    install_requires=[],
    entry_points={
                    'console_scripts': ['a2pcej=a2pcej:main',
                                        ],
                },
    )
