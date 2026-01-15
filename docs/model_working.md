# Model Working – Quantum Density Matrix Reconstruction

## 1. Problem Overview
The objective of this project is to reconstruct a physically valid quantum density matrix ρ from measurement data obtained via Pauli measurements. The reconstructed density matrix must strictly satisfy all physical constraints required of quantum states:
- Hermiticity
- Positive Semi-Definiteness (PSD)
- Unit Trace

The task is framed as a supervised learning problem, where synthetic measurement data is generated from known quantum states and used to train a model capable of learning the inverse mapping from measurements to density matrices.

---

## 2. Track Selection and Model Choice
This project follows **Track 1 (Classical Shadows)** as specified in the assignment.

Instead of a transformer or graph neural network, a fully connected neural network (MLP) architecture is used to map classical measurement expectation values to density matrix parameters. This design choice prioritizes:
- Numerical stability
- Simplicity of implementation
- Full reproducibility
- Ease of enforcing physical constraints

The model takes as input expectation values derived from Pauli measurements and outputs a set of real-valued parameters corresponding to a lower-triangular matrix representation.

---

## 3. Model Architecture
The neural network consists of multiple fully connected layers with nonlinear activations. The final output layer produces parameters used to construct a **lower triangular complex matrix L**, which is later used to reconstruct the density matrix.

Key architectural characteristics:
- Input: Pauli measurement expectation values
- Hidden layers: Fully connected layers with nonlinear activation functions
- Output: Parameters encoding the lower-triangular Cholesky matrix

This architecture allows the model to learn a smooth and differentiable mapping from classical measurement data to valid quantum states.

---

## 4. Physical Constraint Enforcement via Cholesky Decomposition
To ensure that all reconstructed density matrices are physically valid, constraints are enforced **by construction** using the Cholesky decomposition.

The model outputs parameters used to construct a lower triangular complex matrix L. The density matrix is then reconstructed as:

\[
\rho = \frac{LL^\dagger}{\mathrm{Tr}(LL^\dagger)}
\]

This formulation guarantees:
- **Hermiticity**: Since \( LL^\dagger \) is Hermitian
- **Positive Semi-Definiteness**: Since \( LL^\dagger \) is PSD for any matrix L
- **Unit Trace**: Enforced through explicit trace normalization

This approach avoids post-processing corrections and ensures physical validity throughout training and inference.

---

## 5. Loss Function and Training Objective
The model is trained using the **Frobenius norm loss** between the predicted density matrix \( \rho_{\text{pred}} \) and the ground truth density matrix \( \rho_{\text{true}} \):

\[
\mathcal{L} = \| \rho_{\text{pred}} - \rho_{\text{true}} \|_F^2
\]

The Frobenius loss is fully differentiable and numerically stable, making it suitable for gradient-based optimization.

Although **Quantum Fidelity** and **Trace Distance** are physically meaningful metrics, they involve eigenvalue decompositions whose gradients are ill-defined in the complex-valued case. Therefore:
- These metrics are **not used during training**
- They are computed **only during evaluation**

This design choice ensures stable training while still reporting physically relevant performance metrics.

---

## 6. Evaluation Metrics
The trained model is evaluated using the following metrics:
- **Quantum Fidelity** between predicted and true density matrices
- **Trace Distance** between predicted and true density matrices
- **Inference Latency**, measured as the time taken to reconstruct a single density matrix

These metrics provide a comprehensive assessment of reconstruction accuracy and computational efficiency.

---

## 7. Summary
This model implements a physically grounded approach to quantum state reconstruction by combining classical machine learning with constraint-enforcing mathematical structure. By using Cholesky decomposition and trace normalization, the model guarantees physically valid density matrices while maintaining full differentiability and reproducibility.

The design adheres strictly to the requirements of Track 1 and provides a robust, interpretable, and reproducible solution to the quantum density matrix reconstruction problem.
