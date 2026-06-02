
import numpy as np
import numpy.typing as npt

def normalize(vector: npt.ArrayLike) -> npt.NDArray:
    vector = np.asarray(vector, dtype=float)
    if vector.ndim != 1:
        raise ValueError("vector must be 1D array")

    if np.all(vector == 0):
        raise ValueError("vector can't be zero")

    return vector / np.linalg.norm(vector)


vector_np = np.array([1, 2, 3, 4])
vector_norm = normalize(vector=vector_np)
print('Vector:', vector_np)
print('Lenght of vector:', np.linalg.norm(vector_np), '\n')
print('Normalize vector:', vector_norm)
print('Lenght of normalize vector:', np.linalg.norm(vector_norm))
