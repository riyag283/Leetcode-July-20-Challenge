import math 

def findRoots(s): 
    a = 1
    b = 1
    c = -2*s
    d = 1 - 4 * c 
    sqrt_val = math.sqrt(abs(d))  
    if d > 0:
        x = (-1 + sqrt_val)/2 
    elif d == 0: 
        x = -1/2
    else: 
        x = -1
    if x > 0:
        return math.floor(x)
    else:
        return -1
  
# Driver Program 
sum = 6
findRoots(6) 
