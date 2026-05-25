# Реализация скалярного произведения

def dotProduct(vec1: list, vec2: list):
    if len(vec1) != len(vec2): raise ValueError('Vectors have different size.')
    if len(vec1) == 0 and len(vec2) == 0: return 0
    result = 0
    for  i in range(0, len(vec1)):
        result += vec1[i]*vec2[i]
    
    return result