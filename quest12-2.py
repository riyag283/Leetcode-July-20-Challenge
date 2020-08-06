def funct(n):
    binary = "{:b}".format(n)
    extra = 32 - len(binary)
    result = ''
    for i in range(extra):
        result = '0' + result
    for each in binary:
        result = each + result
    return int(result,2)

print(funct(4294967293))
