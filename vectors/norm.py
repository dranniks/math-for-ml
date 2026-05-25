# Реализация функции norm без использования numpy

def norm(v: list[float], p = 2):
    Lp = 0
    if len(v) == 0:
        return 0
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