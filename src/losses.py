import torch

# -------------------------------
# Matrix square root (Hermitian, batched)
# -------------------------------
def sqrtm(rho):
    """
    Computes matrix square root for a batch of Hermitian matrices
    rho: (B, N, N) complex Hermitian
    """
    eigvals, eigvecs = torch.linalg.eigh(rho)

    # Clamp for numerical stability
    eigvals = torch.clamp(eigvals, min=0.0)

    # Convert eigenvalues to complex BEFORE diag_embed
    sqrt_eigvals = torch.sqrt(eigvals).to(torch.cfloat)

    return (
        eigvecs
        @ torch.diag_embed(sqrt_eigvals)
        @ eigvecs.conj().transpose(-1, -2)
    )


# -------------------------------
# Quantum Fidelity
# -------------------------------
def quantum_fidelity(rho, sigma):
    """
    Uhlmann fidelity:
    F(ρ, σ) = (Tr( sqrt( sqrt(ρ) σ sqrt(ρ) ) ))^2
    """
    sqrt_rho = sqrtm(rho)
    inner = sqrt_rho @ sigma @ sqrt_rho
    sqrt_inner = sqrtm(inner)

    fidelity = torch.real(
        torch.diagonal(sqrt_inner, dim1=-2, dim2=-1).sum(-1)
    ) ** 2

    return fidelity


# -------------------------------
# Trace Distance
# -------------------------------
def trace_distance(rho, sigma):
    """
    D(ρ, σ) = 1/2 ||ρ − σ||_1
    """
    diff = rho - sigma
    eigvals = torch.linalg.eigvals(diff)
    return 0.5 * torch.sum(torch.abs(eigvals), dim=-1)

