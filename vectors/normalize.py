
import numpy as np
import numpy.typing as npt

def normalize(vector: npt.NDArray) -> npt.NDArray:

    if vector.ndim != 1:
        raise ValueError("vector must be 1D array")
    
    return vector / np.linalg.norm(vector)


vector_np = np.array([1, 2, 4, 3])
vector_norm = normalize(vector=vector_np)
print('Vector:', vector_np)
print('Lenght of vector:', np.linalg.norm(vector_np), '\n')
print('Normalize vector:', vector_norm)
print('Lenght of normalize vector:', np.linalg.norm(vector_norm))
