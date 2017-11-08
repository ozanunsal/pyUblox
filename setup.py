# coding: utf-8

from setuptools import setup, find_packages

NAME = "ublox"
VERSION = "0.0.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

setup(
    name=NAME,
    version=VERSION,
    description="python uBlox module",
    author_email="matthias.turber@iis.fraunhofer.de",
    url="https://github.com/Fraunhofer-IIS/pyUblox",
    keywords=["uBlox", "ubx"],
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    long_description=""" """
)
