"""
Setup script for TDL Validator package.
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="tdl-validator",
    version="1.0.0",
    author="Pedro A. Pernías Peco",
    author_email="p.pernias@gmail.com",
    description="Validation tools for TDL (Tutor Description Language) files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ppernias/tdl-spec",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Education",
        "Topic :: Software Development :: Quality Assurance",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pyyaml>=6.0",
        "jsonschema>=4.17",
    ],
    entry_points={
        "console_scripts": [
            "tdl-validate=tdl_validator.cli:main",
        ],
    },
    include_package_data=True,
    package_data={
        "": ["*.json", "*.yaml"],
    },
)
