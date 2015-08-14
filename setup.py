import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest-hearts',
    license='MIT',
    description='<3 in your pytest',
    long_description=read("README.md"),
    version='0.3',
    py_modules=['pytest_hearts'],
    entry_points={'pytest11': ['hearts = pytest_hearts']},
    install_requires=['pytest>=2.0'],
)
