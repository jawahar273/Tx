#!/usr/bin/env python
from setuptools import setup, find_packages
from os import path

from version import __version__

with open("README.rst") as readme_file:
    readme = readme_file.read()

with open("HISTORY.rst") as history_file:
    history = history_file.read()

with open(
    path.join(path.dirname(path.abspath(__file__)), "requirements.txt")
) as requirement_file:
    requirements = requirement_file.read().split("/n")

setup_requirements = ["pytest-runner"]

with open(
    path.join(path.dirname(path.abspath(__file__)), "requirements-dev.txt")
) as dev_requirement_file:
    test_requirements = dev_requirement_file.read().split("/n")

setup(
    author="Jawahar S",
    author_email="jawahar273@gmail.com",
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Programming Language :: Python :: 3.7",
    ],
    description="Tx",
    install_requires=requirements,
    long_description=readme + "\n\n" + history,
    include_package_data=True,
    keywords="Tx",
    name="Tx",
    packages=find_packages(include=["Tx", "TxBot"]),
    entry_points={
        'console_scripts': [
            'tx = tui.__main__:main'
        ]
    },
    setup_requires=setup_requirements,
    test_suite="tests",
    tests_require=test_requirements,
    url="https://github.com/jawahar273/Tx",
    version=__version__,
    zip_safe=True,
)
