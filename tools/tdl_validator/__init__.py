"""
TDL Validator - Validation tools for TDL (Tutor Description Language) files.

This package provides validation functionality for TDL files including:
- Instructional Models
- Learning Sequences
- Engine configurations

Usage:
    from tdl_validator import TDLValidator

    validator = TDLValidator()
    result = validator.validate_file('my_sequence.yaml')

    if result.is_valid:
        print("File is valid!")
    else:
        for error in result.errors:
            print(f"Error: {error}")
"""

__version__ = "1.0.0"
__author__ = "Pedro A. Pernías Peco"

from .validator import TDLValidator, ValidationResult
from .cli import main as cli_main

__all__ = ["TDLValidator", "ValidationResult", "cli_main"]
