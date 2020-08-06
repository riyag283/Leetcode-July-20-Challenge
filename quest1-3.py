import math

def solutions(n):
    x = -1
    d = 1 + 8*n
    if d > 0:
        x = (-1 + math.sqrt(abs(d)))/2
    if x > 0:
        return math.floor(x)
    else:
        return 0
