# TDL: A Four-Layer Architecture for LLM-Based Tutors

## Abstract

The deployment of Large Language Models (LLMs) as educational tutors requires more than conversational ability; it demands systematic specification of pedagogical behavior. Research documents that LLMs are not "good tutors by default": they provide direct answers instead of guiding learning through productive challenges.

This paper presents **TDL (Tutor Description Language)**, a four-layer architecture for specifying LLM-based tutors that explicitly separates instructional methodology from content. TDL evolved from practical experience with ADL 1.0 (Assistant Description Language), whose limitations in educational contexts motivated key design decisions.

We identify five structural limitations of ADL 1.0: monolithic architecture, implicit pedagogy, embedded content, implicit boundaries, and lack of inheritance—and show how TDL addresses them through a layered design with explicit Instructional Models aligned with Gagné's instructional events and Bloom's taxonomy.

The design patterns introduced in TDL informed the subsequent development of ADL 2.0, which generalized the inheritance and boundary mechanisms. We demonstrate that TDL's pedagogical decoupling can be expressed as an ADL 2.0 profile without loss of expressiveness, validating the pattern's applicability to other assistant domains.

The specification is portable across ChatGPT, Claude, Gemini, and OpenWebUI. We present two reference instructional models, validation tools, and propose research hypotheses for the empirical validation of TDL's impact on learning outcomes and instructor workload.

## Paper

📄 **[TDL_Paper.pdf](./TDL_Paper.pdf)** - Full academic paper

## Citation

```bibtex
@article{pernias2025tdl,
  title={TDL: A Four-Layer Architecture for LLM-Based Tutors with Decoupled Instructional Methodology},
  author={Pernías Peco, Pedro A. and Escobar Esteban, María P.},
  year={2025}
}
```

## Authors

- **Pedro A. Pernías Peco** - Universidad de Alicante
- **María P. Escobar Esteban** - Universidad de Alicante
