
import numpy as np

def svd_2x2_singular_values(A: np.ndarray) -> tuple:
    A = np.asarray(A, dtype=float)

    if A.shape != (2, 2):
        raise ValueError("A must be a 2x2 matrix")

    B = A.T @ A
    a, b, d = B[0, 0], B[0, 1], B[1, 1]

    if b == 0:
        c, s = 1.0, 0.0
    else:
        tau = (d - a) / (2 * b)
        t = np.copysign(1.0, tau) / (
            abs(tau) + np.sqrt(1 + tau * tau)
        )
        c = 1 / np.sqrt(1 + t * t)
        s = t * c

    V = np.array([[c, s], [-s, c]])
    eigenvalues = np.diag(V.T @ B @ V)
    order = np.argsort(eigenvalues)[::-1]

    V = V[:, order]
    S = np.sqrt(np.maximum(eigenvalues[order], 0.0))

    U = np.zeros((2, 2))
    for i in range(2):
        if S[i] > 1e-12:
            U[:, i] = A @ V[:, i] / S[i]

    if S[0] > 1e-12 and S[1] <= 1e-12:
        U[:, 1] = np.array([-U[1, 0], U[0, 0]])
    elif S[0] <= 1e-12:
        U = np.eye(2)

    return U, S, V.T
