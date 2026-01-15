# AI Usage Disclosure

## Overview
This project made limited and transparent use of AI-assisted tools during development. The purpose of using AI tools was to improve understanding, debug technical issues, and ensure correctness of implementation. All AI-generated suggestions were manually reviewed, tested, and verified before being incorporated into the final submission.

---

## AI Tools Used
The following AI tools were used during the development process:
- ChatGPT (for conceptual clarification, debugging guidance, and documentation assistance)

No AI tools were used for automated code generation without human verification.

---

## Purpose of AI Assistance
AI assistance was used for the following purposes:
- Debugging PyTorch tensor shape and datatype errors
- Understanding how to enforce physical constraints on density matrices
- Clarifying numerical stability issues related to complex-valued eigen-decompositions
- Structuring documentation to meet project deliverable requirements

---

## Example Prompts Used
The following are representative examples of prompts used during development:
- *"Fix PyTorch batched trace error in density matrix reconstruction"*
- *"How to enforce positive semi-definiteness and unit trace using Cholesky decomposition in PyTorch?"*
- *"Why is quantum fidelity unstable for backpropagation in neural networks?"*
- *"Fix complex eigenvalue gradient error in PyTorch linalg.eigh"*
- *"How to structure documentation for a quantum machine learning project?"*

These prompts were used only for guidance and learning support.

---

## Verification and Validation
All AI-assisted outputs were verified through:
- Manual code inspection
- Execution of training and evaluation scripts
- Physical validity checks (Hermiticity, PSD, unit trace)
- Consistency of reported metrics across multiple runs

Only AI-generated suggestions that were validated through successful execution and physical correctness checks were retained.

---

## Statement of Responsibility
The final codebase, experimental results, documentation, and conclusions represent the author's own work. AI tools were used strictly as auxiliary aids and not as substitutes for understanding or independent implementation.
