# TDL Schemas

This directory contains JSON Schema definitions for validating TDL files. Each schema is available in both JSON and YAML format.

## Available Schemas

| Schema | JSON | YAML | Description |
|--------|------|------|-------------|
| **Instructional Model** | `instructional_model.schema.json` | `instructional_model.schema.yaml` | Validates pedagogical models |
| **Learning Sequence** | `learning_sequence.schema.json` | `learning_sequence.schema.yaml` | Validates course definitions |
| **Engine** | `engine.schema.json` | `engine.schema.yaml` | Validates engine configuration |

## Usage

### With the TDL Validator (recommended)

```bash
pip install tdl-validator
tdl-validate my_sequence.yaml --schema learning_sequence
```

### With Python jsonschema

```python
import yaml
import jsonschema

# Load the schema
with open('learning_sequence.schema.json') as f:
    schema = json.load(f)

# Load your TDL file
with open('my_sequence.yaml') as f:
    data = yaml.safe_load(f)

# Validate
jsonschema.validate(data, schema)
```

### With IDE Support (VS Code)

Add this to the top of your YAML file to enable validation:

```yaml
# yaml-language-server: $schema=./spec/schemas/learning_sequence.schema.yaml
```

## Schema Details

### Instructional Model (`instructional_model.schema.json`)

Validates files that define pedagogical methodology:

- **Required fields**: `model.id`, `model.name`, `model.version`, `model.events`
- **Events**: Minimum 2 events required
- **Event IDs**: Must match pattern `E[0-9]+_[A-Z]+` (e.g., `E1_ACTIVATE`)
- **Transition triggers**: Must be one of: `student_response_received`, `comprehension_verified`, `explicit_command`, `auto`

### Learning Sequence (`learning_sequence.schema.json`)

Validates files that define course structure:

- **Required fields**: `sequence.id`, `sequence.name`, `sequence.version`, `sequence.extends`, `sequence.tutor_profile`, `sequence.learning_units`
- **extends**: Must reference a `.yaml` or `.yml` file
- **Learning unit IDs**: Must match pattern `LU[0-9]+` (e.g., `LU1`, `LU2`)
- **Bloom levels**: `remember`, `understand`, `apply`, `analyze`, `evaluate`, `create`

### Engine (`engine.schema.json`)

Validates engine configuration files:

- **Required fields**: `engine.version`, `engine.name`, `engine.state_tracking`, `engine.commands`
- **Commands**: At minimum, `start` command is required
- **Command syntax**: Must match pattern `/[a-z]+` (e.g., `/start`, `/next`)

## JSON Schema Version

All schemas use JSON Schema Draft 2020-12.

## Contributing

If you find issues with the schemas or want to propose extensions, please open an issue or PR on GitHub.
