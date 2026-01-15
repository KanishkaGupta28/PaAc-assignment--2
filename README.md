# PAAC Assignment 2 – Quantum State Tomography using Neural Networks

This repository contains the complete implementation for **PAAC Assignment 2**,
focused on reconstructing single-qubit quantum states using a neural-network-based
approach to **Quantum State Tomography (QST)**.

The project includes dataset generation, model definition, training, evaluation,
and comprehensive documentation to ensure full reproducibility and transparency.

---

## Project Overview

Quantum State Tomography aims to reconstruct the density matrix of a quantum system
from measurement outcomes.  
In this assignment, a neural network is trained to map measurement statistics
derived from Pauli measurements to a physically valid single-qubit density matrix.

Key objectives:
- Learn a valid density matrix representation
- Enforce physical constraints (Hermiticity, PSD, unit trace)
- Evaluate reconstruction accuracy and fidelity
- Ensure reproducibility and responsible AI usage

---

## Repository Structure
```
PaAC_Assignment 2/
│
├── docs/
│ ├── model_working.md # Model architecture and theory
│ ├── replication_guide.md # Step-by-step reproduction instructions
│ └── AI_USAGE.md # AI usage disclosure
│
├── outputs/
│ └── model.pt # Trained model checkpoint
│
├── src/
│ ├── data_generation.py # Synthetic dataset generation
│ ├── model.py # Neural network model definition
│ ├── losses.py # Physically motivated loss functions
│ ├── train.py # Training script
│ ├── evaluate.py # Evaluation and validation script
│ ├── train_data.pkl # Serialized training data
│ └── test_data.pkl # Serialized test data
│
├── requirements.txt # Python dependencies
├── AI_USAGE.md # AI usage disclosure (root copy)
└── README.md # Project overview (this file)
```

---

## Installation

### 1. Clone or Extract the Repository
Ensure you are in the project root directory.

### 2. Create Virtual Environment
```
python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate
```

### 3. Install Dependencies
```
pip install -r requirements.txt
```
### 4. Usage
-Train the Model
`python src/train.py`
-This will:
-Load the training dataset
-Train the neural network
-Save the trained model to `outputs/model.pt`

### 5.Evaluate the Model
`python src/evaluate.py`
-This performs:
-Reconstruction accuracy evaluation
-Fidelity computation
-Physical validity checks on predicted density matrices

## Reproducibility

Full replication instructions are provided in:
- 📄 `docs/replication_guide.md`

This includes:
- Environment setup  
- Deterministic dataset generation  
- Training and evaluation steps  
- Verification checklist  

## Model Documentation

Detailed explanation of:
- Network architecture  
- Density matrix parameterization  
- Loss functions  
- Physical constraints enforcement  

- 📄 `docs/model_working.md`

## AI Usage Disclosure

This project follows responsible AI usage practices.

- 📄 `AI_USAGE.md`  
- 📄 `docs/AI_USAGE.md`  

AI tools were used strictly as auxiliary aids and not as substitutes for
understanding, implementation, or validation.

## Results

Evaluation was performed on the held-out test dataset using the trained model.

- Mean Quantum Fidelity: **0.9724**
- Mean Trace Distance: **0.0831**
- Average Inference Latency: **1.92 ms per sample**

Metrics were computed using standard quantum information definitions and averaged across the test set.

## Results Summary

The trained model reconstructs physically valid single-qubit density matrices.

Output states satisfy:
- Hermiticity  
- Positive semi-definiteness  
- Unit trace  

Evaluation confirms stable and consistent reconstruction performance.

Exact metrics and validation procedures are documented in `model_working.md`.

## Notes

- No GPU is required  
- All data is synthetic and self-contained  
- Internet access is not required after dependency installation  

