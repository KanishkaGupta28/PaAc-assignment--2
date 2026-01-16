# Final Report  
**QCG × PaAC Open Project — Winter 2025–2026**  
**Assignment 2**

---

## 1. Objective

The objective of this project is to design and train a computational model capable of reconstructing a valid quantum density matrix \( \rho \) from measurement data. The reconstructed density matrix must strictly satisfy all physical constraints:

- **Hermitian**
- **Positive Semi-Definite**
- **Unit Trace**

The project emphasizes physically valid reconstruction, reproducibility, and rigorous quantitative evaluation.

---

## Model Overview

This project follows **Track 1 (Classical Shadows)**.

Instead of predicting the density matrix directly, the model outputs the parameters of a **lower-triangular matrix** \( L \).  
The density matrix is reconstructed using the **Cholesky decomposition**:

$$
\rho = \frac{L L^\dagger}{\mathrm{Tr}(L L^\dagger)}
$$

This parameterization guarantees:

- **Hermiticity** by construction  
- **Positive semi-definiteness**  
- **Unit trace** via explicit normalization  

The model is trained using **synthetically generated single-qubit measurement data** derived from randomly sampled valid quantum states.


---

## 3. Evaluation Metrics

Model performance is evaluated on a held-out test dataset using the following standard quantum information metrics:

- **Quantum Fidelity**
- **Trace Distance**
- **Inference Latency**

These metrics quantify reconstruction accuracy as well as computational efficiency.

---

## 4. Quantitative Results

The following results were obtained by running `evaluate.py` on the trained model:

| Metric | Value |
|------|------|
| **Mean Fidelity** | **0.9471** |
| **Mean Trace Distance** | **0.1475** |
| **Inference Latency** | **1.25 ms per reconstruction** |

---

## 5. Discussion

- The high mean fidelity indicates strong agreement between reconstructed and ground-truth quantum states.
- The low trace distance further confirms accurate quantum state estimation.
- The low inference latency demonstrates that the model is computationally efficient and suitable for fast reconstruction tasks.

All physical constraints are strictly enforced through the Cholesky-based formulation, eliminating the need for post-processing corrections.

---

## 6. Reproducibility

This project is fully reproducible. The repository includes:

- Source code for dataset generation, training, and evaluation
- Saved model weights in the `outputs/` directory
- A detailed replication guide in `replication_guide.md`
- Environment dependencies listed in `requirements.txt`

All commands are designed to be executed from the project root directory.

---

## 7. AI Usage Disclosure

## AI Attribution

AI-assisted tools were used during development in compliance with the project’s transparency requirements.

Full disclosure, prompt descriptions, and verification methodology are documented in `AI_USAGE.md`.

---

## 8. Conclusion

This work demonstrates a robust and physically grounded machine learning approach for quantum state reconstruction. By enforcing quantum constraints at the architectural level, the model achieves high accuracy, stability, and efficiency, meeting all requirements of the QCG × PaAC Open Project Assignment 2.

---




