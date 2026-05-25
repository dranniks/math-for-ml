# Реализация функции norm без использования numpy

def norm(v: list[float], p = 2):
    Lp = 0
    if len(v) == 0:
        return 'Array is empty.'
    if p < 1:
        return "'p' is less than 1"
    # L1-норма
    if p == 1:
        for i in range(0, len(v)):
            Lp += abs(v[i])
        
        return Lp
    
    # L2-норма, Евклидова норма
    elif p == 2:
        for i in range(0, len(v)):
            Lp += pow(v[i], 2)
        
        Lp = pow(Lp, 0.5)
        return Lp
    
    # Max-норма, бесконечная норма
    elif p == float('inf'):
        Lp = max(v, key=abs)
        return abs(Lp)
    
    # Общий случай
    else:
        for i in range(0, len(v)):
            Lp += pow(abs(v[i]), p)
        
        Lp = pow(Lp, 1/p)
        return Lp
    


import numpy as np

v = [3, -4, 2]
ps = [1, 2, float('inf'), 3]

for p in ps:
    my_result = norm(v, p)
    np_result = np.linalg.norm(v, ord=p)

    print(f"p = {p}")
    print(f"my norm:    {my_result}")
    print(f"numpy norm: {np_result}")
    print(f"equal:      {np.isclose(my_result, np_result)}")
    print()