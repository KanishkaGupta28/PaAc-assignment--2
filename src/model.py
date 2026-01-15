import torch
import torch.nn as nn
import torch.nn.functional as F

# -------------------------------
# Measurement Encoder
# -------------------------------
class MeasurementEncoder(nn.Module):
    """
    Encodes Pauli basis and measurement outcomes into embeddings
    """
    def __init__(self, embed_dim=32):
        super().__init__()
        self.basis_embedding = nn.Embedding(3, embed_dim)   # X, Y, Z
        self.outcome_embedding = nn.Embedding(2, embed_dim)  # -1, +1

    def forward(self, basis, outcome):
        b_emb = self.basis_embedding(basis)
        o_emb = self.outcome_embedding(outcome)
        return b_emb + o_emb


# -------------------------------
# Transformer-based QST Model
# -------------------------------
class QSTTransformer(nn.Module):
    """
    Transformer model that predicts Cholesky parameters
    """
    def __init__(self, embed_dim=32, num_heads=4, num_layers=2):
        super().__init__()

        self.encoder = MeasurementEncoder(embed_dim)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=embed_dim,
            nhead=num_heads,
            batch_first=True
        )

        self.transformer = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )

        self.output_layer = nn.Linear(embed_dim, 4)

    def forward(self, basis, outcome):
        """
        basis   : (B, T)  ∈ {0,1,2}
        outcome : (B, T)  ∈ {0,1}
        """
        x = self.encoder(basis, outcome)
        x = self.transformer(x)
        x = x.mean(dim=1)
        params = self.output_layer(x)
        return params


# -------------------------------
# Cholesky Reconstruction
# -------------------------------
def reconstruct_density_matrix(params):
    """
    Reconstructs a valid density matrix using Cholesky decomposition

    params: (B, 4) → [a, b, c, d]
    """
    a, b, c, d = params[:, 0], params[:, 1], params[:, 2], params[:, 3]

    B = params.shape[0]
    L = torch.zeros((B, 2, 2), dtype=torch.cfloat, device=params.device)

    # Enforce positivity on diagonal via softplus
    L[:, 0, 0] = F.softplus(a)
    L[:, 1, 0] = b + 1j * c
    L[:, 1, 1] = F.softplus(d)

    # Construct density matrix
    rho = L @ L.conj().transpose(-1, -2)

    # Batched trace normalization (FIXED)
    trace = torch.real(
        torch.diagonal(rho, dim1=-2, dim2=-1).sum(-1)
    )

    rho = rho / trace.view(-1, 1, 1)

    return rho
