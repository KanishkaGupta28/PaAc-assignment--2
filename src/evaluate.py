import pickle
import time
import torch
import numpy as np
from torch.utils.data import DataLoader, Dataset

from model import QSTTransformer, reconstruct_density_matrix
from losses import quantum_fidelity, trace_distance
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# -------------------------------
# Dataset
# -------------------------------
class ShadowDataset(Dataset):
    def __init__(self, data_path):
        with open(data_path, "rb") as f:
            self.data = pickle.load(f)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        item = self.data[idx]

        basis_map = {"X": 0, "Y": 1, "Z": 2}
        basis = torch.tensor([basis_map[b] for b, _ in item["measurements"]])
        outcome = torch.tensor([1 if o == 1 else 0 for _, o in item["measurements"]])

        rho = torch.tensor(item["rho"], dtype=torch.cfloat)
        return basis, outcome, rho

# -------------------------------
# Evaluation
# -------------------------------
def evaluate():
    device = torch.device("cpu")

    model = QSTTransformer().to(device)
    model.load_state_dict(
    torch.load(os.path.join(BASE_DIR, "..", "outputs", "model.pt"))
)

    model.eval()

    test_loader = DataLoader(
        ShadowDataset(os.path.join(BASE_DIR, "test_data.pkl")),
        batch_size=1,
        shuffle=False
    )

    fidelities = []
    trace_distances = []
    latencies = []

    with torch.no_grad():
        for basis, outcome, rho_true in test_loader:
            basis = basis.to(device)
            outcome = outcome.to(device)
            rho_true = rho_true.to(device)

            start = time.time()
            params = model(basis, outcome)
            rho_pred = reconstruct_density_matrix(params)
            end = time.time()

            fidelities.append(
                quantum_fidelity(rho_pred, rho_true).item()
            )

            trace_distances.append(
                trace_distance(rho_pred, rho_true).item()
            )

            latencies.append(end - start)

    print("===== Evaluation Results =====")
    print(f"Mean Fidelity       : {np.mean(fidelities):.4f}")
    print(f"Mean Trace Distance : {np.mean(trace_distances):.4f}")
    print(f"Inference Latency   : {np.mean(latencies)*1000:.2f} ms")

# -------------------------------
if __name__ == "__main__":
    evaluate()
