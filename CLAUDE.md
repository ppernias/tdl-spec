# Project Context for Claude

## Project Overview

This repository (`tdl-spec`) contains the **public specification** of TDL (Tutor Description Language) v1.0.

**Related repository**: `ppernias/tdl10` (private) contains the academic paper and development work.

## The Connection Between Spec and Paper

The TDL specification and the academic paper are deeply connected:

1. **The paper** (`tdl10/main.tex`) provides the theoretical foundation, research context, and formal analysis
2. **The spec** (`tdl-spec/`) provides the practical, usable implementation

When working on either:
- Changes to the spec should be consistent with claims in the paper
- The paper's Section V (Components) and Section VI (Instructional Models) contain the authoritative examples
- Any new features should be reflected in both

## Key Architectural Decisions

### Four-Layer Architecture
```
Engine → Instructional Model → Learning Sequence → Content Source
```

Each layer has a specific owner and purpose. This separation is **fundamental** to TDL's design.

### Chronological Context: ADL 1.0 → TDL → ADL 2.0

TDL was developed as an evolution of ADL 1.0 for educational use cases. The limitations identified in ADL 1.0 informed both:
- TDL's domain-specific solutions (Instructional Model, Content Source layers)
- ADL 2.0's general solutions (Core/Profile separation, extends mechanism)

This chronology is important for understanding design decisions.

### Five Limitations of ADL 1.0 (Addressed by TDL/ADL 2.0)

| Limitation | Scope | Solution |
|------------|-------|----------|
| L1. Monolithic architecture | General | ADL 2.0 Core/Profile |
| L2. Implicit pedagogy | Domain-specific | TDL Instructional Model |
| L3. Embedded content | Domain-specific | TDL Content Source |
| L4. Implicit boundaries | General | ADL 2.0 boundaries |
| L5. No inheritance | General | ADL 2.0 extends |

## Files to Keep Synchronized

When updating the spec, ensure consistency with:

| Spec File | Paper Reference |
|-----------|-----------------|
| `spec/examples/engine_v1.2.yaml` | Section V.B |
| `spec/examples/instructional_model_bloom8.yaml` | Section VI |
| `spec/examples/learning_sequence_example.yaml` | Section V.D |
| `README.md` architecture diagram | Section IV, Figure 1 |

## Terminology

Use these terms consistently:

- **Engine**: The execution layer (not "runtime" or "interpreter")
- **Instructional Model**: The "how to teach" (not "pedagogical template")
- **Learning Sequence**: The course definition (not "curriculum" or "syllabus")
- **Content Source**: Reference material (not "knowledge base")
- **extends**: The inheritance mechanism (lowercase, as YAML key)

## Paper Status

- **Current version**: English, IEEE format, 10 sections
- **Branch**: `main` in `tdl10` repository
- **Overleaf**: Synchronized with `tdl10/main`
- **Spanish backup**: `spanish-original` branch in `tdl10`

## Future Work Items

From the paper's Section X:

1. [ ] TDL Maker (visual editor)
2. [ ] Learning analytics hooks
3. [ ] Community repository of models
4. [ ] Assessment extensions
5. [ ] Lightweight student model
6. [ ] LMS integration
7. [ ] Formal ADL 2.0 profile definition
