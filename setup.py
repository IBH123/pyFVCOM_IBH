#!/usr/bin/env python

from setuptools import setup, find_packages
import os

# Read the README file for the long description
def read_readme():
    readme_path = os.path.join(os.path.dirname(__file__), 'README.md')
    if os.path.exists(readme_path):
        with open(readme_path, 'r', encoding='utf-8') as f:
            return f.read()
    return ""

# Read version from __init__.py
def get_version():
    version_file = os.path.join(os.path.dirname(__file__), '__init__.py')
    if os.path.exists(version_file):
        with open(version_file, 'r') as f:
            for line in f:
                if line.startswith('__version__'):
                    return line.split('=')[1].strip().strip('"\'')
    return "2.2.0-fixed"

setup(
    name="PyFVCOM-fixed",
    version=get_version(),
    author="PyFVCOM Contributors (Fixed Version)",
    author_email="your-email@example.com",
    description="PyFVCOM with critical bug fixes for modern Python environments",
    long_description=read_readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/pyFVCOM",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Oceanography",
    ],
    python_requires=">=3.8",
    install_requires=[
        "numpy>=1.19.0",
        "scipy>=1.5.0",
        "matplotlib>=3.3.0",
        "netCDF4>=1.5.0",
        "pyproj>=3.0.0",
        "shapely>=1.7.0",
        "pandas>=1.1.0",
        "pytz",
        "python-dateutil",
        "xlsxwriter",
        "lxml",
        "jdcal",
        "networkx",
        "pyshp",
        "UTide",
        "descartes",
        "contourpy",
    ],
    extras_require={
        "dev": [
            "pytest",
            "pytest-cov",
            "black",
            "flake8",
        ],
    },
    package_data={
        "": ["*.md", "*.txt", "*.rst"],
    },
    include_package_data=True,
    zip_safe=False,
)