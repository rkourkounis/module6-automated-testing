from pkg_resources import parse_requirements
from setuptools import setup

install_reqs = parse_requirements('requirements.txt')

setup(
    name='module6_cyb600',
    version='1.0.2',
    author_email='kourkouk@canisius.edu',
    author='Riley Kourkounis',
    packages=['cyb600_module6'],
    tests=['tests'],
    license='Apache License Version 2.0',
)
