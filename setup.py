import os
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(
    name='pytest-love',
    license='MIT',
    description='Green progress dots',
    long_description=read("README.md"),
    version='0.3',
    py_modules=['pytest_love'],
    entry_points={'pytest11': ['love = pytest_love']},
    install_requires=['pytest>=2.0', 'blessings'],
)
