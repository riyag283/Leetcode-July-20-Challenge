def func(x,y):
    xor = x^y
    count = 0
    while xor > 0:
        if xor & 1:
            count += 1
        xor >>= 1
    return count

print(func(1,4))
