def func(s):
    s = s.split()
    rev = []
    for idx in range(len(s)-1, -1, -1):
        rev.append(s[idx])
    return ' '.join(rev)

print(func('Hello Miki, Me Mini'))
print(func("  hello world!  "))
