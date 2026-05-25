import numpy as np
from norm import norm
from dotProduct import dotProduct

def cosine(vec1: list, vec2: list):
    norm1 = norm(vec1)
    norm2 = norm(vec2)

    if norm1 == 0 or norm2 == 0: 
        raise ValueError("Cosine similarity is undefined for zero vector.")

    return dotProduct(vec1, vec2) / (norm1 * norm2)

def  cosineNP(a, b):
    return (a @ b)/(np.linalg.norm(a) * np.linalg.norm(b))

import random

for i in range(10):
    vec1 = [random.randint(-10, 10) for _ in range(3)]
    vec2 = [random.randint(-10, 10) for _ in range(3)]

    print(i, ":", cosine(vec1, vec2))
    print("np:", cosineNP(np.array(vec1), np.array(vec2)))
    print()