#َalireza noori 40113200057
import numpy as np
from scipy.linalg import lu, lu_factor, lu_solve

# Function to get a matrix from the user
def get_matrix():
    rows = int(input("Number of rows: "))
    cols = int(input("Number of columns: "))
    matrix = []
    print("Enter the elements of the matrix:")
    for _ in range(rows):
        row = []
        for _ in range(cols):
            element = float(input())
            row.append(element)
        matrix.append(row)
    return np.array(matrix)

# Get the matrices A, B, and C
print("\nStep 1 : \n")
print("Matrix A:")
A = get_matrix()

print("Matrix B:")
B = get_matrix()

print("Matrix C:")
C = get_matrix()

# Calculate the results
try:
    A_plus_B = A + B
    A_minus_B = A - B
    A_plus_C = A + C
    A_minus_C = A - C
    B_plus_C = B + C
    B_minus_C = B - C
    A_times_B = np.dot(A, B)
    B_times_A = np.dot(B, A)
    A_times_C = np.dot(A, C)
    C_times_A = np.dot(C, A)
    B_times_C = np.dot(B, C)
    C_times_B = np.dot(C, B)
except ValueError:
    print("A + B is not calculable.")
    print("A - B is not calculable.")
    print("A + C is not calculable.")
    print("A - C is not calculable.")
    print("B + C is not calculable.")
    print("B - C is not calculable.")
    print("A * B is not calculable.")
    print("B * A is not calculable.")
    print("A * C is not calculable.")
    print("C * A is not calculable.")
    print("B * C is not calculable.")
    print("C * B is not calculable.")
else:
    print("A + B:")
    print(A_plus_B)

    print("A - B:")
    print(A_minus_B)

    print("A + C:")
    print(A_plus_C)

    print("A - C:")
    print(A_minus_C)

    print("B + C:")
    print(B_plus_C)

    print("B - C:")
    print(B_minus_C)

    print("A * B:")
    print(A_times_B)

    print("B * A:")
    print(B_times_A)

    print("A * C:")
    print(A_times_C)

    print("C * A:")
    print(C_times_A)

    print("B * C:")
    print(B_times_C)

    print("C * B:")
    print(C_times_B)

# Get the column vector b
print("\nStep 2 : \n")
print("Column vector b:")
b_rows = int(input("Number of rows: "))
b = []
print("Enter the elements of the vector:")
for _ in range(b_rows):
    element = float(input())
    b.append(element)
b = np.array(b).reshape(-1, 1)

# Solve the systems
try:
    x_A = np.linalg.solve(A, b)
    x_B = np.linalg.solve(B, b)
    x_C = np.linalg.solve(C, b)
except np.linalg.LinAlgError:
    print("System Ax=b is unsolvable.")
    print("System Bx=b is unsolvable.")
    print("System Cx=b is unsolvable.")
else:
    print("Solution for Ax = b:")
    print(x_A)

    print("Solution for Bx = b:")
    print(x_B)

    print("Solution for Cx = b:")
    print(x_C)

# Matrix invertibility
print("\nStep 3 : \n")
def is_invertible(matrix):
    try:
        inv_matrix = np.linalg.inv(matrix)
        return True, inv_matrix
    except np.linalg.LinAlgError as e:
        return False, str(e)

A_invertible, A_inv = is_invertible(A)
B_invertible, B_inv = is_invertible(B)
C_invertible, C_inv = is_invertible(C)

if A_invertible:
    print("Matrix A is invertible.")
    print(A_inv)
else:
    print("Matrix A is not invertible.")

if B_invertible:
    print("Matrix B is invertible.")
    print(B_inv)
else:
    print("Matrix B is not invertible.")

if C_invertible:
    print("Matrix C is invertible.")
    print(C_inv)
else:
    print("Matrix C is not invertible.")


# Function to perform LU decomposition and check squareness
def lu_decomposition(matrix):
    try:
        P, L, U = lu(matrix)
        is_square = True
        return is_square, P, L, U
    except np.linalg.LinAlgError:
        is_square = False
        return is_square, None, None

# LU decomposition and squareness check for matrices A, B, and C
A_is_square, A_P, A_L, A_U = lu_decomposition(A)
B_is_square, B_P, B_L, B_U = lu_decomposition(B)
C_is_square, C_P, C_L, C_U = lu_decomposition(C)
print("\nStep 4 : ")
if A_is_square:
    print("\nMatrix A is square.")
    print("LU decomposition of A:")
    print(f"\nP:\n{A_P}\nL:\n{A_L}\nU:\n{A_U}")
else:
    print("\nMatrix A is not square.")

if B_is_square:
    print("\nMatrix B is square.")
    print("LU decomposition of B:")
    print(f"\nP:\n{B_P}\nL:\n{B_L}\nU:\n{B_U}")
else:
    print("\nMatrix B is not square.")

if C_is_square:
    print("\nMatrix C is square.")
    print("LU decomposition of C:")
    print(f"\nP:\n{C_P}\nL:\n{C_L}\nU:\n{C_U}")
else:
    print("\nMatrix C is not square.")