"""Setup for the chocobo package."""

import setuptools


with open('README.md') as f:
    README = f.read()

setuptools.setup(
    author="Owen Smith",
    author_email="owen8461@protonmail.com",
    name='raster-indices-calc',
    license="MIT",
    description='chocobo is a python package for delicious chocobo recipes.',
    version='v0.0.3',
    long_description=README,
    url='https://github.com/shaypal5/chocobo',
    packages=setuptools.find_packages(),
    python_requires=">=3.5",
    install_requires=['requests'],
    classifiers=[
        # Trove classifiers
        # (https://pypi.python.org/pypi?%3Aaction=list_classifiers)
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
    ],
)