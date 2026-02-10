# TDL: Tutor Description Language

**TDL** (Tutor Description Language) is a YAML-based domain-specific language for creating LLM-powered educational tutors with explicit pedagogical methodology.

## What is TDL?

TDL provides a four-layer architecture that separates:

| Layer | Purpose | Who Creates It |
|-------|---------|----------------|
| **Engine** | Execution semantics, commands, state tracking | TDL maintainers |
| **Instructional Model** | How to teach (pedagogical events) | Instructional designers |
| **Learning Sequence** | What to teach (course structure) | Teachers |
| **Content Source** | Reference material | Content experts |

This separation enables:
- **Reusability**: One instructional model works across many courses
- **Portability**: Same files work on ChatGPT, Claude, Gemini, OpenWebUI
- **Collaboration**: Different experts handle different layers
- **Transparency**: YAML files are human-readable and auditable

## Quick Example

```yaml
# Learning Sequence (what the teacher creates)
sequence:
  id: "intro-to-python"
  name: "Introduction to Python"
  extends: "instructional_model_bloom8.yaml"  # Inherit pedagogy

  tutor_profile:
    name: "Py"
    personality: |
      Patient coding mentor who loves analogies.
      Never gives answers directly; guides discovery.

  learning_units:
    - id: "LU1"
      title: "Variables and Data Types"
      objectives:
        - level: "understand"
          description: "Explain what a variable is"
      prompt: |
        Analogy: Variables are like labeled boxes.
        Cover: int, float, str, bool
        Common mistake: confusing = with ==
```

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         ENGINE                               │
│   Commands (/start, /next) • State Tracking • Security      │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   INSTRUCTIONAL MODEL                        │
│   E1: Activate → E2: Objectives → E3: Explain → E4: Verify  │
│   → E5: Example → E6: Practice → E7: Connect → E8: Summarize│
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    LEARNING SEQUENCE                         │
│   Tutor Profile • Behaviors • Learning Units (LU1→LU2→...)  │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                     CONTENT SOURCE                           │
│   Reference material in Markdown with ## Section: headers   │
└─────────────────────────────────────────────────────────────┘
```

## Getting Started

### 1. Choose an Instructional Model

Start with a pre-built model from `spec/examples/`:
- `instructional_model_bloom8.yaml` - Comprehensive 8-step model for deep learning
- More models coming soon

### 2. Create Your Learning Sequence

```yaml
sequence:
  id: "my-course"
  name: "My Course Name"
  extends: "instructional_model_bloom8.yaml"

  tutor_profile:
    name: "TutorName"
    personality: "Describe the tutor's style..."

  learning_units:
    - id: "LU1"
      title: "First Topic"
      prompt: "What to teach and how..."
      next: "LU2"

    - id: "LU2"
      title: "Second Topic"
      prompt: "..."
      next: null  # End of course
```

### 3. Deploy to Your Platform

| Platform | Engine Location | TDL Files Location |
|----------|-----------------|-------------------|
| ChatGPT GPTs | Instructions | Knowledge |
| Claude Projects | Project Instructions | Project Knowledge |
| Gemini Gems | Instructions | Attached Files |
| OpenWebUI | System Prompt | Knowledge + RAG |

## Repository Structure

```
tdl-spec/
├── README.md                 # This file
├── spec/
│   ├── examples/             # Ready-to-use examples
│   │   ├── engine_v1.2.yaml
│   │   ├── instructional_model_bloom8.yaml
│   │   ├── learning_sequence_example.yaml
│   │   └── content_generative_ai.md
│   ├── schemas/              # JSON Schemas for validation
│   └── engine/               # Engine reference implementation
├── tools/                    # Validation and utilities
└── docs/                     # Papers and documentation
    └── TDL_Paper.pdf         # Academic paper describing TDL
```

## Theoretical Foundation

TDL is grounded in established instructional design theories:

- **Gagné's Nine Events of Instruction**: The instructional model events map to Gagné's framework
- **Bloom's Taxonomy**: Learning objectives use Bloom levels (remember, understand, apply, analyze, evaluate, create)
- **Merrill's First Principles**: Focus on problem-centered learning with activation, demonstration, application, and integration

## Alignment with ADL 2.0

TDL is designed to be compatible with **ADL 2.0** (Assistant Description Language), a core specification framework for LLM-based assistants. TDL can be expressed as an ADL 2.0 profile, demonstrating that:

- TDL's inheritance mechanism maps to ADL 2.0's `extends`
- TDL's four layers align with ADL 2.0's Core/Profile separation
- TDL's pedagogical decoupling validates ADL 2.0's extensibility

See the academic paper in `docs/` for detailed analysis.

## Contributing

Contributions are welcome! Areas where help is needed:

- [ ] Additional instructional models (Problem-Based Learning, Socratic Method, etc.)
- [ ] JSON Schema definitions for validation
- [ ] Python validator tool
- [ ] Visual editor (TDL Maker)
- [ ] Translations of documentation

## License

[To be determined - likely MIT or CC-BY]

## Citation

If you use TDL in academic work, please cite:

```bibtex
@article{pernias2025tdl,
  title={TDL: A Four-Layer Architecture for LLM-Based Tutors with Decoupled Instructional Methodology},
  author={Pernías Peco, Pedro A. and Escobar Esteban, María P.},
  journal={[Journal]},
  year={2025}
}
```

## Contact

- **Author**: Pedro A. Pernías Peco
- **Email**: p.pernias@gmail.com
- **Paper**: See `docs/TDL_Paper.pdf`
