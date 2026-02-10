# TDL Validator

A Python tool for validating TDL (Tutor Description Language) files against JSON Schema definitions.

## Installation

### From Source

```bash
cd tools
pip install -e .
```

### Dependencies Only

```bash
pip install pyyaml jsonschema
```

## Usage

### Command Line

```bash
# Validate a single file (auto-detects type)
tdl-validate my_sequence.yaml

# Validate with explicit type
tdl-validate my_model.yaml --type instructional_model

# Validate a sequence with its referenced model
tdl-validate my_sequence.yaml --model my_model.yaml

# Validate all files in a directory
tdl-validate ./my_course/

# Validate recursively
tdl-validate ./my_course/ --recursive

# Quiet mode (only show errors)
tdl-validate *.yaml --quiet

# Verbose mode (show warnings)
tdl-validate *.yaml --verbose
```

### Python API

```python
from tdl_validator import TDLValidator

# Create validator
validator = TDLValidator()

# Validate a single file
result = validator.validate_file('my_sequence.yaml')
print(result)  # ✓ my_sequence.yaml is valid (learning_sequence)

if not result.is_valid:
    for error in result.errors:
        print(f"Error: {error}")

# Validate with explicit schema type
result = validator.validate_file('my_model.yaml', schema_type='instructional_model')

# Validate sequence with its model
result = validator.validate_sequence_with_model(
    'my_sequence.yaml',
    'my_model.yaml'
)

# Validate all files in a directory
results = validator.validate_directory('./my_course/', recursive=True)
for result in results:
    print(result)

# Validate data directly (without file)
data = {
    'sequence': {
        'id': 'my-course',
        'name': 'My Course',
        # ...
    }
}
result = validator.validate_data(data)
```

## Validation Rules

### Instructional Model

- `model.id`: lowercase with hyphens (e.g., `bloom-8step-interactive`)
- `model.version`: semantic version (e.g., `1.0`, `1.0.1`)
- `model.events`: minimum 2 events required
- Event `id`: pattern `E[0-9]+_[A-Z]+` (e.g., `E1_ACTIVATE`)
- Transition triggers: `student_response_received`, `comprehension_verified`, `explicit_command`, `auto`

### Learning Sequence

- `sequence.id`: lowercase with hyphens
- `sequence.extends`: must end in `.yaml` or `.yml`
- `sequence.tutor_profile`: requires `name` and `personality`
- Learning unit `id`: pattern `LU[0-9]+` (e.g., `LU1`)
- Bloom levels: `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create`

### Engine

- `engine.version`: semantic version
- `engine.commands.start`: required
- Command `syntax`: pattern `/[a-z]+` (e.g., `/start`)

## Exit Codes

| Code | Meaning |
|------|---------|
| 0 | All files valid |
| 1 | Validation errors found |
| 2 | Other errors (missing files, schema errors, etc.) |

## Custom Schema Directory

If you want to use custom schemas:

```bash
tdl-validate my_file.yaml --schema-dir /path/to/schemas/
```

```python
validator = TDLValidator(schema_dir='/path/to/schemas/')
```

## Development

Run tests:

```bash
pytest tests/
```

## License

MIT License
