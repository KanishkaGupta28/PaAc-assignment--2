import numpy as np
import pickle
from tqdm import tqdm

# -------------------------------
# Pauli matrices
# -------------------------------
PAULI_MATRICES = {
    "X": np.array([[0, 1], [1, 0]], dtype=complex),
    "Y": np.array([[0, -1j], [1j, 0]], dtype=complex),
    "Z": np.array([[1, 0], [0, -1]], dtype=complex),
}

# -------------------------------
# Generate random single-qubit state
# -------------------------------
def random_density_matrix():
    psi = np.random.randn(2) + 1j * np.random.randn(2)
    psi = psi / np.linalg.norm(psi)
    rho = np.outer(psi, psi.conj())
    return rho

# -------------------------------
# Simulate Pauli measurement
# -------------------------------
def measure_pauli(rho, pauli):
    P = PAULI_MATRICES[pauli]
    expectation = np.real(np.trace(rho @ P))
    prob_plus = (1 + expectation) / 2
    outcome = np.random.choice([1, -1], p=[prob_plus, 1 - prob_plus])
    return outcome

# -------------------------------
# Generate dataset
# -------------------------------
def generate_dataset(num_states=500, shots=50):
    dataset = []
    paulis = ["X", "Y", "Z"]

    for _ in tqdm(range(num_states)):
        rho = random_density_matrix()
        measurements = []

        for _ in range(shots):
            basis = np.random.choice(paulis)
            outcome = measure_pauli(rho, basis)
            measurements.append((basis, outcome))

        dataset.append({
            "rho": rho,
            "measurements": measurements
        })

    return dataset

# -------------------------------
# Main
# -------------------------------
if __name__ == "__main__":
    np.random.seed(42)

    train_data = generate_dataset(num_states=1000, shots=50)
    test_data = generate_dataset(num_states=200, shots=50)

    with open("train_data.pkl", "wb") as f:
        pickle.dump(train_data, f)

    with open("test_data.pkl", "wb") as f:
        pickle.dump(test_data, f)

    print("✅ Dataset generated successfully")
