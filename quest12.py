def funct(n):
    binary = ''
    while n > 0:
        if n & 1:
            binary += '1'
        else:
            binary += '0'
        n >>= 1
    return int(binary,2)

#binary = '11101'
#print(int(binary,2))
print(funct(4294967293))
