import numpy as np

def analyze_matrix():
    rows, cols = 4, 5
    matrix = np.zeros((rows, cols), dtype=int)

    # Generate matrix with row-based ranges
    for i in range(rows):
        matrix[i] = np.random.randint(i + 1, i + 10, size=cols)

    print("Generated Matrix:\n", matrix)

    # Row-wise statistics
    row_mean = np.mean(matrix, axis=1)
    row_std = np.std(matrix, axis=1)

    # Column-wise statistics
    col_mean = np.mean(matrix, axis=0)
    col_std = np.std(matrix, axis=0)

    # Overall comparison
    overall_row_mean = np.mean(row_mean)
    overall_col_mean = np.mean(col_mean)

    overall_row_std = np.mean(row_std)
    overall_col_std = np.mean(col_std)

    # Final result
    result = {
        "mean": "row-wise" if overall_row_mean > overall_col_mean else "column-wise",
        "std": "row-wise" if overall_row_std > overall_col_std else "column-wise"
    }

    return result

outcome = analyze_matrix()
print("\nFinal Outcome Dictionary:")
print(outcome)
