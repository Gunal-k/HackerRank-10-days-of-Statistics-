def transpose(matrix):
    rows, cols = len(matrix), len(matrix[0])
    return [[matrix[j][i] for j in range(rows)] for i in range(cols)]

def multiply_matrices(A, B):
    rows_A, cols_A = len(A), len(A[0])
    cols_B = len(B[0])

    # Result matrix initialization
    result = [[0] * cols_B for _ in range(rows_A)]

    # Optimized multiplication
    for i in range(rows_A):
        for k in range(cols_A):
            for j in range(cols_B):
                result[i][j] += A[i][k] * B[k][j]
    
    return result

def gaussian_elimination(A, B):
    """Solves Ax = B using Gaussian elimination (without explicit inversion)."""
    size = len(A)

    # Convert A into an augmented matrix [A | B]
    for i in range(size):
        A[i] += B[i]  # Append B as last column

    # Forward elimination
    for i in range(size):
        # Find pivot
        max_row = max(range(i, size), key=lambda r: abs(A[r][i]))
        A[i], A[max_row] = A[max_row], A[i]

        pivot = A[i][i]

        # Normalize row
        A[i] = [x / pivot for x in A[i]]

        # Eliminate column
        for j in range(i + 1, size):
            factor = A[j][i]
            A[j] = [A[j][k] - factor * A[i][k] for k in range(size + 1)]

    # Back substitution
    x = [0] * size
    for i in range(size - 1, -1, -1):
        x[i] = A[i][-1] - sum(A[i][j] * x[j] for j in range(i + 1, size))

    return [[xi] for xi in x]

def solve_linear_regression(F, N, train, target, test):
    # Step 1: Add a bias column (1) to the training data
    X = [[1] + row for row in train]  # Add bias term
    Y = [[y] for y in target]  # Convert Y into a column matrix

    # Step 2: Compute X^T * X
    X_T = transpose(X)
    XTX = multiply_matrices(X_T, X)

    # Step 3: Compute X^T * Y
    XTY = multiply_matrices(X_T, Y)

    # Step 4: Solve for B using Gaussian elimination (instead of inversion)
    B = gaussian_elimination(XTX, XTY)

    # Flatten B (convert from list of lists to a single list)
    B = [b[0] for b in B]

    # Step 5: Predict values for test cases
    test = [[1] + row for row in test]  # Add bias term
    predictions = [sum(B[i] * x[i] for i in range(F + 1)) for x in test]

    return predictions

# Read input
F, N = map(int, input().split())

# Read training data
train = []
target = []

for _ in range(N):
    data = list(map(float, input().split()))
    train.append(data[:F])  # Features
    target.append(data[F])  # Output Y

# Read test data
n = int(input())
test = [list(map(float, input().split())) for _ in range(n)]

# Solve regression
predictions = solve_linear_regression(F, N, train, target, test)

# Print results
for y in predictions:
    print(round(y, 2))