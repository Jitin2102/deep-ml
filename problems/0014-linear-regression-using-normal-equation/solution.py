import numpy as np

def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X = np.array(X)
    y = np.array(y)

    d = X.T @ X
    dinv = np.linalg.inv(d)

    theta = dinv @ X.T @ y

    return theta.tolist()