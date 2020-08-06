def func(s):
    revs = []
    word = ''
    s += ' '
    for l in s:
        if l != ' ':
            word += l
        else:
            revs.append(word)
            word = ''
    revs2 = [value for value in revs if value != '']
    revs2.reverse()
    #print(revs2)
    return ' '.join(revs2)

print(func('Hello Miki, Me Mini'))
print(func("  hello world!  "))
