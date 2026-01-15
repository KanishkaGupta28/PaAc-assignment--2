# Replication Guide

This document provides a complete, step-by-step guide to reproduce all results
reported in **PAAC Assignment 2**.  
Following the instructions below will allow an independent evaluator to
recreate the training process, saved model artifacts, and evaluation results
from scratch.

---

## 1. System Requirements

The experiments were developed and tested under the following environment:

- **Operating System**: Windows 10 / 11 (64-bit)
- **Python Version**: Python 3.10 or later
- **Hardware**:
  - CPU: Any modern CPU (no GPU required)
  - RAM: ≥ 8 GB recommended
- **Disk Space**: ~500 MB free space

No GPU acceleration is required for this project.

---

## 2. Repository Structure

Ensure the repository has the following structure before proceeding:
```
PaAC_Assignment 2/
│
├── docs/
│ ├── model_working.md
│ ├── AI_USAGE.md
│ └── replication_guide.md
│
├── outputs/
│ └── model.pt
│
├── src/
│ ├── data_generation.py
│ ├── model.py
│ ├── losses.py
│ ├── train.py
│ ├── evaluate.py
│ ├── train_data.pkl
│ └── test_data.pkl
│
├── requirements.txt
├── AI_USAGE.md
└── README.md
```

---

## 3. Environment Setup

### 3.1 Create Virtual Environment (Recommended)

From the project root directory:

```bash
python -m venv venv
```
- Activate the virtual environment:
```
-Windows (PowerShell):
.\venv\Scripts\Activate.ps1
- Windows (Command Prompt):
.\venv\Scripts\activate
```
### 3.2 Install Dependencies

-Install all required Python packages:
```
pip install -r requirements.txt

-Verify successful installation by running:

python -c "import torch; print(torch.__version__)"
```
## 4. Dataset Preparation

This project uses synthetically generated quantum measurement data.

### 4.1 Data Files

The following files are already included for reproducibility:

- `src/train_data.pkl` — Training dataset  
- `src/test_data.pkl` — Test dataset  

If regeneration is required, run:
```bash
python src/data_generation.py
```
### 5. Model Training
-To train the model from scratch:
-`python src/train.py`
-Expected Output
-Training progress printed to the console
-Final trained model saved as:
-`outputs/model.pt`
-A successful run ends with a message similar to:

✅ Model saved to outputs/model.pt

## 6. Model Evaluation

After training (or using the provided model), run evaluation:
```bash
python src/evaluate.py
```
**Evaluation Outputs**:
-Fidelity and reconstruction error metrics printed to the console
-Physical validity checks including:
-Hermiticity
-Positive semi-definiteness
-Unit trace condition

## 7. Reproducibility Controls

The following steps ensure deterministic and reproducible results:

- Fixed random seeds are set in:
  - `data_generation.py`
  - `train.py`

- Deterministic PyTorch behavior is enforced where applicable  
- Identical train/test splits are reused via serialized `.pkl` files  
- No stochastic layers (e.g., dropout) are used during evaluation  

Re-running training under the same environment will yield numerically consistent results.

## 8. Verification Checklist

To verify successful replication, ensure:

- `model.pt` is generated in `outputs/`  
- Training completes without runtime errors  
- Evaluation metrics are finite and physically valid  
- Density matrices satisfy Hermiticity, positive semi-definiteness (PSD), and unit trace  
- Results match those described in `model_working.md`

## 9. Common Issues and Fixes

**Issue:** `ModuleNotFoundError`  
**Fix:** Ensure the virtual environment is activated and all dependencies are installed.

---

**Issue:** Autograd error involving eigen-decomposition  
**Fix:** Use the provided loss functions in `losses.py`, which avoid ill-defined gradients for complex eigenvectors.

---

**Issue:** Permission error when activating the virtual environment  
**Fix (PowerShell):**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass

## 10. Notes for Evaluators

- All scripts are self-contained and require no external datasets.  
- The project does not rely on internet access after dependency installation.  
- The saved model (`model.pt`) can be evaluated directly without retraining.

## 11. Contact and Attribution

This project was developed as part of **PAAC Assignment 2**.  
All implementation, validation, and analysis decisions were made by the author.  
AI tools were used only as auxiliary aids, as disclosed in `AI_USAGE.md`.
