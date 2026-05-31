def add_matrix(matrix1, matrix2):
    # Check if matrices have the same dimensions
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return "Matrices are not equal"

    result = []

    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0])):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


matrix1 = [
    [1, 2, 3],
    [6, 7, 8]
]

matrix2 = [
    [4, 5, 6],
    [7, 8, 9]
]

result_matrix = add_matrix(matrix1, matrix2)

if isinstance(result_matrix, str):
    print(result_matrix)
else:
    print("Sum of matrices:")
    for row in result_matrix:
        print(row)    
