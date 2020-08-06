def arrangeCoins(n):
    total = n
    i = 0
    curr = 0
    while True:
        i += 1
        total -= i
        if total < 0:
            break
        curr = i
    return curr

n = 8
print(arrangeCoins(n))
