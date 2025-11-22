#范權榮 111210557
import numpy as np


# ============================================================
# 1. Recursive Determinant (Pure Python, Laplace Expansion)
# ============================================================

def recursive_determinant(A):
    """
    Computes determinant recursively using cofactor expansion.
    A is a list of lists.
    """
    n = len(A)

    # Base cases
    if n == 1:
        return A[0][0]
    if n == 2:
        return A[0][0]*A[1][1] - A[0][1]*A[1][0]

    det = 0
    for col in range(n):
        # Create the minor matrix
        minor = [row[:col] + row[col+1:] for row in A[1:]]
        sign = (-1) ** col
        det += sign * A[0][col] * recursive_determinant(minor)

    return det



# ============================================================
# 2. LU Decomposition (Doolittle, No Pivoting)
# ============================================================

def lu_decomposition(A):
    """
    Perform LU decomposition: A = L @ U
    """
    A = A.astype(float)
    n = A.shape[0]

    L = np.zeros((n, n))
    U = np.zeros((n, n))

    for i in range(n):

        # Compute U row
        for k in range(i, n):
            s = sum(L[i][j] * U[j][k] for j in range(i))
            U[i][k] = A[i][k] - s

        # Compute L column
        L[i][i] = 1
        for k in range(i+1, n):
            s = sum(L[k][j] * U[j][i] for j in range(i))
            L[k][i] = (A[k][i] - s) / U[i][i]

    return L, U



# ============================================================
# 3. Determinant via LU: det(A) = product of diagonal(U)
# ============================================================

def determinant_lu(A):
    L, U = lu_decomposition(A)
    return np.prod(np.diag(U))



# ============================================================
# 4. Verification: LU, Eigen, SVD Reconstruction
# ============================================================

def verify_decompositions(A):
    print("\n===== ORIGINAL MATRIX A =====")
    print(A)

    # --- LU ---
    L, U = lu_decomposition(A)
    print("\n===== L =====")
    print(L)
    print("\n===== U =====")
    print(U)
    print("\nLU Reconstruction (L@U):\n", L @ U)

    # --- Eigen ---
    w, V = np.linalg.eig(A)
    A_eigen = V @ np.diag(w) @ np.linalg.inv(V)
    print("\n===== Eigenvalues =====")
    print(w)
    print("\n===== Eigenvectors =====")
    print(V)
    print("\nEigen Reconstruction:\n", A_eigen)

    # --- SVD ---
    U_svd, S_svd, Vt_svd = np.linalg.svd(A)
    A_svd = U_svd @ np.diag(S_svd) @ Vt_svd
    print("\n===== U (SVD) =====")
    print(U_svd)
    print("\n===== S (SVD) =====")
    print(S_svd)
    print("\n===== V^T (SVD) =====")
    print(Vt_svd)
    print("\nSVD Reconstruction:\n", A_svd)



# ============================================================
# 5. SVD from Eigen Decomposition (manual SVD)
# ============================================================

def svd_from_eig(A):
    """
    Compute SVD using only eigen decomposition:
    A^T A = V diag(S^2) V^T
    A V = U S
    """
    ATA = A.T @ A

    eigvals, V = np.linalg.eig(ATA)

    # Sort by eigenvalue descending
    idx = eigvals.argsort()[::-1]
    eigvals = eigvals[idx]
    V = V[:, idx]

    # Singular values
    S = np.sqrt(np.abs(eigvals))

    # Compute U = A V / S
    U = (A @ V) / S

    return U, S, V.T



# ============================================================
# 6. PCA (Principal Component Analysis)
# ============================================================

def PCA(X, k):
    """
    PCA using eigen decomposition of covariance matrix.
    """
    X = np.array(X, float)

    # Step 1: center data
    X_centered = X - np.mean(X, axis=0)

    # Step 2: covariance matrix
    cov = np.cov(X_centered, rowvar=False)

    # Step 3: eigen decomposition
    w, V = np.linalg.eig(cov)

    # Step 4: sort by importance
    idx = np.argsort(w)[::-1]
    w = w[idx]
    V = V[:, idx]

    # Step 5: project data
    X_pca = X_centered @ V[:, :k]

    return X_pca, w, V



# ============================================================
# Test / Example Section
# ============================================================

if __name__ == "__main__":

    A = np.array([[4, 2],
                  [3, 1]], float)

    # ---------------------------
    # 1. Recursive determinant
    # ---------------------------
    A_list = A.tolist()
    print("\n1. Recursive Determinant =", recursive_determinant(A_list))

    # ---------------------------
    # 2 & 3. LU and LU determinant
    # ---------------------------
    print("\n2. LU Decomposition:")
    L, U = lu_decomposition(A)
    print("L =\n", L)
    print("U =\n", U)

    print("\n3. Determinant via LU =", determinant_lu(A))

    # ---------------------------
    # 4. Verification of all decompositions
    # ---------------------------
    verify_decompositions(A)

    # ---------------------------
    # 5. SVD from eigenvalues
    # ---------------------------
    print("\n===== 5. SVD from Eigen Decomposition =====")
    U_eig, S_eig, Vt_eig = svd_from_eig(A)
    print("U =\n", U_eig)
    print("S =", S_eig)
    print("V^T =\n", Vt_eig)

    # ---------------------------
    # 6. PCA Example
    # ---------------------------
    print("\n===== 6. PCA Example =====")
    X = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ], float)

    X_pca, eigenvalues, eigenvectors = PCA(X, k=1)
    print("Projected Data (k=1):\n", X_pca)
    print("Eigenvalues:\n", eigenvalues)
    print("Eigenvectors:\n", eigenvectors)
