"""
Command-line interface for TDL Validator.
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from .validator import TDLValidator, ValidationResult


def create_parser() -> argparse.ArgumentParser:
    """Create the argument parser."""
    parser = argparse.ArgumentParser(
        prog='tdl-validate',
        description='Validate TDL (Tutor Description Language) files',
        epilog='For more information, visit: https://github.com/ppernias/tdl-spec'
    )

    parser.add_argument(
        'files',
        nargs='+',
        help='TDL file(s) to validate (YAML format)'
    )

    parser.add_argument(
        '-t', '--type',
        choices=['instructional_model', 'learning_sequence', 'engine', 'auto'],
        default='auto',
        help='Type of TDL file (default: auto-detect)'
    )

    parser.add_argument(
        '-m', '--model',
        help='Path to instructional model file (for validating sequences with their model)'
    )

    parser.add_argument(
        '-s', '--schema-dir',
        help='Directory containing schema files (default: bundled schemas)'
    )

    parser.add_argument(
        '-r', '--recursive',
        action='store_true',
        help='If a directory is given, search recursively'
    )

    parser.add_argument(
        '-q', '--quiet',
        action='store_true',
        help='Only output errors, no success messages'
    )

    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show detailed output including warnings'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 1.0.0'
    )

    return parser


def print_result(result: ValidationResult, quiet: bool = False, verbose: bool = False) -> None:
    """Print a validation result."""
    if result.is_valid:
        if not quiet:
            print(f"✓ {result.file_path}")
            if verbose and result.file_type:
                print(f"  Type: {result.file_type}")
    else:
        print(f"✗ {result.file_path}")
        for error in result.errors:
            print(f"  ERROR: {error}")

    if verbose and result.warnings:
        for warning in result.warnings:
            print(f"  WARNING: {warning}")


def main(args: Optional[List[str]] = None) -> int:
    """
    Main entry point for the CLI.

    Args:
        args: Command line arguments (uses sys.argv if None)

    Returns:
        Exit code (0 for success, 1 for validation errors, 2 for other errors)
    """
    parser = create_parser()
    parsed = parser.parse_args(args)

    # Initialize validator
    try:
        validator = TDLValidator(schema_dir=parsed.schema_dir)
    except ImportError as e:
        print(f"Error: {e}", file=sys.stderr)
        print("Install required dependencies: pip install pyyaml jsonschema", file=sys.stderr)
        return 2
    except Exception as e:
        print(f"Error initializing validator: {e}", file=sys.stderr)
        return 2

    # Determine schema type
    schema_type = None if parsed.type == 'auto' else parsed.type

    # Collect all results
    all_results: List[ValidationResult] = []

    for file_or_dir in parsed.files:
        path = Path(file_or_dir)

        if path.is_dir():
            # Validate all files in directory
            results = validator.validate_directory(str(path), recursive=parsed.recursive)
            all_results.extend(results)
        elif path.is_file():
            # Validate single file
            if parsed.model and schema_type in (None, 'learning_sequence'):
                result = validator.validate_sequence_with_model(str(path), parsed.model)
            else:
                result = validator.validate_file(str(path), schema_type)
            all_results.append(result)
        else:
            all_results.append(ValidationResult(
                is_valid=False,
                file_path=str(path),
                errors=[f"Path not found: {path}"]
            ))

    # Print results
    valid_count = 0
    invalid_count = 0

    for result in all_results:
        print_result(result, quiet=parsed.quiet, verbose=parsed.verbose)
        if result.is_valid:
            valid_count += 1
        else:
            invalid_count += 1

    # Print summary
    if len(all_results) > 1 and not parsed.quiet:
        print()
        print(f"Summary: {valid_count} valid, {invalid_count} invalid")

    # Return appropriate exit code
    return 0 if invalid_count == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
