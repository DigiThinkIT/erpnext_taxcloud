# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from pip.req import parse_requirements
import re, ast

# get version from __version__ variable in erpnext_taxcloud/__init__.py
_version_re = re.compile(r'__version__\s+=\s+(.*)')

with open('erpnext_taxcloud/__init__.py', 'rb') as f:
    version = str(ast.literal_eval(_version_re.search(
        f.read().decode('utf-8')).group(1)))

requirements = parse_requirements("requirements.txt", session="")

setup(
	name='erpnext_taxcloud',
	version=version,
	description='Fetches United State sales tax from TaxCloud.com and updates Quotations, Sales Order & Sales Invoice',
	author='Neil Lasrado',
	author_email='neil@digithinkit.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=[str(ir.req) for ir in requirements],
	dependency_links=[str(ir._link) for ir in requirements if ir._link]
)
