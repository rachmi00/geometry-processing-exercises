# NumPy and SciPy Matrix Operations Example

This project demonstrates basic matrix operations using NumPy and SciPy in Python. It includes element-wise operations, matrix multiplication, solving linear equations, and sparse matrix operations.

## Operations

The following operations are performed on matrices `A`, `B`, and vector `u`:

### 1. Element-wise Operations
- **A + B**: Adds matrices A and B element-wise.
- **B * A**: Multiplies matrices B and A element-wise.
- **A - 3**: Subtracts 3 from each element of matrix A.
- **1 / A**: Performs element-wise division of 1 by each element of matrix A.

### 2. Matrix Multiplication
- **A @ u**: Multiplies matrix A with vector u using matrix multiplication.

### 3. Transpose
- **A.T**: Computes the transpose of matrix A.

### 4. Norms
- **||A||_F**: Computes the Frobenius norm of matrix A.
- **||u||**: Computes the Euclidean norm (L2 norm) of vector u.

### 5. Solving Linear Equations
- **inv(A) @ b**: Solves the system of linear equations `Ax = b` using NumPy's `np.linalg.solve()` function.

### 6. Sparse Matrices
- **Sparse matrix creation**: Creates sparse matrices using SciPy's `sp.sparse.csr_matrix()` for efficient storage.
- **A + B**: Adds two sparse matrices element-wise.
- **A * B**: Multiplies two sparse matrices element-wise.

## Requirements

- Python 3.x
- NumPy library
- SciPy library

To install the required libraries, run:

```bash
pip install numpy scipy
