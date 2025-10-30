
def input_matrix(name):
    print(f"Enter elements for {name} (2x2):")
    matrix = []
    for i in range(2):
        row = list(map(int, input(f"Row {i+1}: ").split()))
        matrix.append(row)
    return matrix

def print_matrix(matrix, title):
    print(f"\n{title}:")
    for row in matrix:
        print(row)

def add_matrices(A, B):
    return [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]

def multiply_matrices(A, B):
    result = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(2))
    return result

def sort_rows_by_sum(matrix):
    return sorted(matrix, key=lambda row: sum(row))

A = input_matrix("Matrix A")
B = input_matrix("Matrix B")

sum_matrix = add_matrices(A, B)
product_matrix = multiply_matrices(A, B)
sorted_matrix = sort_rows_by_sum(product_matrix)

print_matrix(A, "Matrix A")
print_matrix(B, "Matrix B")
print_matrix(sum_matrix, "Sum of A and B")
print_matrix(product_matrix, "Product of A and B")
print_matrix(sorted_matrix, "Product Matrix Sorted by Row Sums")
