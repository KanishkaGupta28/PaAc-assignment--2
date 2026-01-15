import pickle
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader

from model import QSTTransformer, reconstruct_density_matrix

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
        basis = torch.tensor(
            [basis_map[b] for b, _ in item["measurements"]],
            dtype=torch.long
        )

        outcome = torch.tensor(
            [1 if o == 1 else 0 for _, o in item["measurements"]],
            dtype=torch.long
        )

        rho = torch.tensor(item["rho"], dtype=torch.cfloat)
        return basis, outcome, rho


# -------------------------------
# Training
# -------------------------------
def train():
    device = torch.device("cpu")

    model = QSTTransformer().to(device)
    optimizer = torch.optim.Adam(model.parameters(), lr=1e-3)

    train_loader = DataLoader(
        ShadowDataset("train_data.pkl"),
        batch_size=16,
        shuffle=True
    )

    epochs = 20

    for epoch in range(epochs):
        model.train()
        losses = []

        for basis, outcome, rho_true in train_loader:
            basis = basis.to(device)
            outcome = outcome.to(device)
            rho_true = rho_true.to(device)

            params = model(basis, outcome)
            rho_pred = reconstruct_density_matrix(params)

            # 🔑 Frobenius (Hilbert–Schmidt) loss
            loss = torch.mean(
                torch.norm(rho_pred - rho_true, dim=(-2, -1)) ** 2
            )

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            losses.append(loss.item())

        print(
            f"Epoch {epoch+1}/{epochs} | "
            f"Mean Frobenius Loss: {np.mean(losses):.6f}"
        )

    torch.save(model.state_dict(), "../outputs/model.pt")
    print("✅ Model saved to outputs/model.pt")


# -------------------------------
if __name__ == "__main__":
    train()
