import numpy as np

v = np.random.randint(-100, 100, size=100)

def findPerpendicularVector(vector):
    perpendicularVector = np.random.randint(-100, 100, size=100)
    projection = (np.dot(perpendicularVector, vector) / np.dot(vector, vector)) * vector
    perpendicularVector = perpendicularVector - projection

    if np.isclose(np.dot(vector, perpendicularVector), 0):
        return perpendicularVector

print(findPerpendicularVector(v))