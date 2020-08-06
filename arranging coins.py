def func(n):
    left, right = 0, n
    while left <= right:
        k = (left+right)//2
        curr = k*(k+1)//2
        if curr == n:
            return k
        if n < curr:
            right = k-1
        else:
            left = k+1
    return right

print(func(1002))
