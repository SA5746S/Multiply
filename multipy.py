# Simple Matrix Addition and Multiplication

# Input matrix A
rows = int(input("Enter number of rows for Matrix A: "))
cols = int(input("Enter number of columns for Matrix A: "))

print("Enter elements of Matrix A row-wise:")
A = [list(map(int, input().split())) for _ in range(rows)]

# Input matrix B
print("Enter elements of Matrix B row-wise:")
B = [list(map(int, input().split())) for _ in range(rows)]  # For addition, same rows & cols

# Matrix Addition
print("\nSum of matrices:")
sum_matrix = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
for row in sum_matrix:
    print(row)

# Matrix Multiplication
# Input columns for Matrix B
cols_B = int(input("\nEnter number of columns for Matrix B (for multiplication): "))
print("Enter elements of Matrix B row-wise again for multiplication:")
B_mul = [list(map(int, input().split())) for _ in range(rows)]

print("\nProduct of matrices:")
product = [[0 for _ in range(cols_B)] for _ in range(rows)]
for i in range(rows):
    for j in range(cols_B):
        for k in range(cols):
            product[i][j] += A[i][k] * B_mul[k][j]

for row in product:
    print(row)
