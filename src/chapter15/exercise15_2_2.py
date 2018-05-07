from chapter15.textbook15_2 import matrix_multiply


def matrix_chain_multiply(A, s, i, j):
    if i == j:
        return A[i]
    return matrix_multiply(matrix_chain_multiply(A, s, i, s[i, j]), matrix_chain_multiply(A, s, s[i, j] + 1, j))
