"""
Core validation logic for TDL files.
"""

import json
import os
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml

try:
    import jsonschema
    from jsonschema import ValidationError
    # Try to use the latest validator, fall back to older versions
    try:
        from jsonschema import Draft202012Validator as Validator
    except ImportError:
        try:
            from jsonschema import Draft7Validator as Validator
        except ImportError:
            from jsonschema import Draft4Validator as Validator
    HAS_JSONSCHEMA = True
except ImportError:
    HAS_JSONSCHEMA = False
    Validator = None


@dataclass
class ValidationResult:
    """Result of a validation operation."""
    is_valid: bool
    file_path: str
    file_type: Optional[str] = None
    errors: List[str] = field(default_factory=list)
    warnings: List[str] = field(default_factory=list)

    def __str__(self) -> str:
        if self.is_valid:
            return f"✓ {self.file_path} is valid ({self.file_type})"
        else:
            error_list = "\n  - ".join(self.errors)
            return f"✗ {self.file_path} has {len(self.errors)} error(s):\n  - {error_list}"


class TDLValidator:
    """
    Validator for TDL (Tutor Description Language) files.

    Supports validation of:
    - Instructional Models
    - Learning Sequences
    - Engine configurations

    Example:
        validator = TDLValidator()
        result = validator.validate_file('my_sequence.yaml')

        if not result.is_valid:
            for error in result.errors:
                print(error)
    """

    SCHEMA_TYPES = {
        'instructional_model': 'instructional_model.schema.json',
        'learning_sequence': 'learning_sequence.schema.json',
        'engine': 'engine.schema.json',
    }

    def __init__(self, schema_dir: Optional[str] = None):
        """
        Initialize the validator.

        Args:
            schema_dir: Directory containing schema files. If None, uses default location.
        """
        if not HAS_JSONSCHEMA:
            raise ImportError(
                "jsonschema package is required. Install it with: pip install jsonschema"
            )

        if schema_dir is None:
            # Look for schemas relative to this file
            package_dir = Path(__file__).parent.parent.parent
            schema_dir = package_dir / "spec" / "schemas"

        self.schema_dir = Path(schema_dir)
        self._schemas: Dict[str, dict] = {}
        self._load_schemas()

    def _load_schemas(self) -> None:
        """Load all schema files."""
        for schema_type, filename in self.SCHEMA_TYPES.items():
            schema_path = self.schema_dir / filename
            if schema_path.exists():
                with open(schema_path, 'r', encoding='utf-8') as f:
                    self._schemas[schema_type] = json.load(f)

    def _detect_file_type(self, data: dict) -> Optional[str]:
        """
        Detect the type of TDL file based on its content.

        Args:
            data: Parsed YAML/JSON data

        Returns:
            File type string or None if unknown
        """
        if 'model' in data:
            return 'instructional_model'
        elif 'sequence' in data:
            return 'learning_sequence'
        elif 'engine' in data:
            return 'engine'
        return None

    def _load_yaml_file(self, file_path: str) -> Dict[str, Any]:
        """Load and parse a YAML file."""
        with open(file_path, 'r', encoding='utf-8') as f:
            return yaml.safe_load(f)

    def validate_data(
        self,
        data: dict,
        schema_type: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate TDL data against a schema.

        Args:
            data: Parsed TDL data (dict)
            schema_type: Type of schema to use. If None, auto-detects.

        Returns:
            ValidationResult with validation outcome
        """
        # Auto-detect type if not specified
        if schema_type is None:
            schema_type = self._detect_file_type(data)

        if schema_type is None:
            return ValidationResult(
                is_valid=False,
                file_path="<data>",
                errors=["Could not detect TDL file type. Expected 'model', 'sequence', or 'engine' key."]
            )

        if schema_type not in self._schemas:
            return ValidationResult(
                is_valid=False,
                file_path="<data>",
                file_type=schema_type,
                errors=[f"Schema not found for type: {schema_type}"]
            )

        schema = self._schemas[schema_type]
        validator = Validator(schema)

        errors = []
        for error in validator.iter_errors(data):
            # Format error message with path
            path = " -> ".join(str(p) for p in error.absolute_path) if error.absolute_path else "root"
            errors.append(f"[{path}] {error.message}")

        return ValidationResult(
            is_valid=len(errors) == 0,
            file_path="<data>",
            file_type=schema_type,
            errors=errors
        )

    def validate_file(
        self,
        file_path: str,
        schema_type: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate a TDL file.

        Args:
            file_path: Path to the YAML file
            schema_type: Type of schema to use. If None, auto-detects.

        Returns:
            ValidationResult with validation outcome
        """
        file_path = str(file_path)

        # Check file exists
        if not os.path.exists(file_path):
            return ValidationResult(
                is_valid=False,
                file_path=file_path,
                errors=[f"File not found: {file_path}"]
            )

        # Load file
        try:
            data = self._load_yaml_file(file_path)
        except yaml.YAMLError as e:
            return ValidationResult(
                is_valid=False,
                file_path=file_path,
                errors=[f"YAML parsing error: {e}"]
            )
        except Exception as e:
            return ValidationResult(
                is_valid=False,
                file_path=file_path,
                errors=[f"Error reading file: {e}"]
            )

        # Validate
        result = self.validate_data(data, schema_type)
        result.file_path = file_path

        return result

    def validate_sequence_with_model(
        self,
        sequence_path: str,
        model_path: Optional[str] = None
    ) -> ValidationResult:
        """
        Validate a learning sequence and optionally its referenced instructional model.

        Args:
            sequence_path: Path to the learning sequence file
            model_path: Path to the instructional model file. If None, extracts from 'extends'.

        Returns:
            ValidationResult with combined validation outcome
        """
        # First validate the sequence
        seq_result = self.validate_file(sequence_path, 'learning_sequence')

        if not seq_result.is_valid:
            return seq_result

        # Load sequence to get model reference
        data = self._load_yaml_file(sequence_path)
        extends = data.get('sequence', {}).get('extends')

        if extends and model_path is None:
            # Try to find model relative to sequence
            seq_dir = Path(sequence_path).parent
            model_path = seq_dir / extends

        if model_path and os.path.exists(model_path):
            model_result = self.validate_file(str(model_path), 'instructional_model')

            if not model_result.is_valid:
                seq_result.warnings.append(f"Referenced model has errors: {model_path}")
                seq_result.errors.extend([f"[model] {e}" for e in model_result.errors])
                seq_result.is_valid = False
        elif extends:
            seq_result.warnings.append(f"Referenced model not found: {extends}")

        return seq_result

    def validate_directory(
        self,
        dir_path: str,
        recursive: bool = False
    ) -> List[ValidationResult]:
        """
        Validate all TDL files in a directory.

        Args:
            dir_path: Directory path
            recursive: Whether to search subdirectories

        Returns:
            List of ValidationResult objects
        """
        results = []
        dir_path = Path(dir_path)

        pattern = "**/*.yaml" if recursive else "*.yaml"

        for yaml_file in dir_path.glob(pattern):
            # Skip schema files
            if '.schema.' in yaml_file.name:
                continue

            result = self.validate_file(str(yaml_file))
            results.append(result)

        # Also check .yml files
        pattern = "**/*.yml" if recursive else "*.yml"
        for yml_file in dir_path.glob(pattern):
            if '.schema.' in yml_file.name:
                continue
            result = self.validate_file(str(yml_file))
            results.append(result)

        return results
