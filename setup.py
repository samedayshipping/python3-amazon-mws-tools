from setuptools import setup, find_packages

VERSION = 'v1.0.0'

REQUIREMENTS = [
    'lxml',
    'python-amazon-mws',
    'python-dateutil',
    'requests'
]

PACKAGES = find_packages()

setup(
    name='python3-amazon-mws-tools',
    packages=PACKAGES,
    url='https://github.com/ctaylor4874/python3-amazon-mws-tools',
    license='LICENSE.txt',
    author='Cody Taylor <ctaylor4874@gmail.com>, Mark Sanders <sdscdeveloper@gmail.com>',
    author_email='ctaylor4874@gmail.com, sdscdeveloper@gmail.com',
    install_requires=REQUIREMENTS,
    description='Wrapper modules to request and parse responses for python-amazon-mws.',
    include_package_data=True,
    version=VERSION
)
