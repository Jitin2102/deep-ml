import numpy as np

def compute_norm(arr: np.ndarray, norm_type: str) -> float:
    arr = np.asarray(arr)

    if arr.ndim not in (1, 2):
        raise ValueError("Input must be a 1D or 2D array")

    if norm_type == 'l1':
        return float(np.sum(np.abs(arr)))

    elif norm_type == 'l2':
        return float(np.sqrt(np.sum(arr ** 2)))

    elif norm_type == 'linf':
        return float(np.max(np.abs(arr)))

    elif norm_type == 'frobenius':
        if arr.ndim != 2:
            raise ValueError("Frobenius norm requires a 2D array")
        return float(np.sqrt(np.sum(arr ** 2)))

    else:
        raise ValueError("Invalid norm type")
