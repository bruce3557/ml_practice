
def transpose(A):
    num_rows = len(A)
    num_cols = len(A[0])
    result_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            result_matrix[j][i] = A[i][j]
    
    return result_matrix
