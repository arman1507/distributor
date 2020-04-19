# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in distributor/__init__.py
from distributor import __version__ as version

setup(
	name='distributor',
	version=version,
	description='Fitur Untuk Membuat Purchase Order',
	author='arman',
	author_email='arman150796@gmail.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
