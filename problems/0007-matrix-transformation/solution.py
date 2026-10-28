import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
	if np.linalg.det(T) != 0 and np.linalg.det(S) !=0:
		inv = np.linalg.inv(T)
		p1 = np.dot(inv,A)
		transformed_matrix = np.dot(p1,S)
		return transformed_matrix
	else :
		return -1