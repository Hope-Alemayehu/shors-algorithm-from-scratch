#handles the period finding logic and classical postprocessing
import numpy as np

def qft(state_vector):
    """Apply Quantum Fourier Transform on the given state vector."""
    n = len(state_vector)
    qft_matrix = np.zeros((n, n), dtype=complex)
    omega = np.exp(2j * np.pi / n)
    
    for i in range(n):
        for j in range(n):
            qft_matrix[i, j] = omega ** (i * j) / np.sqrt(n)
    
    return np.dot(qft_matrix, state_vector)
