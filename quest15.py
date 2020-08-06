def func(s):
    revs = ''
    word = ''
    s += ' '
    for l in s:
        if l != ' ':
            word += l
        else:
            revs = word + ' ' + revs
            word = ''
    return revs.strip()

print(func('Hello Miki, Me Mini'))
