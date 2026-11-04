
def determinant_4x4(matrix):
    def det(mat):
        n = len(mat)

        if n == 1:
            return mat[0][0]

        if n == 2:
            return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]

        result = 0

        for j in range(n):
            minor = [
                [mat[i][k] for k in range(n) if k != j]
                for i in range(1, n)
            ]

            result += ((-1) ** j) * mat[0][j] * det(minor)

        return result

    return det(matrix)
