def func(num):
    if num < 10:
        return num
    l = [int(d) for d in str(num)]
    return func(sum(l))

print(func(12668981))
