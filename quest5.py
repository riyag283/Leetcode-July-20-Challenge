num2bits =[0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4]

def count(num):
    nibble = 0
    if 0 == num:
        return num2bits[0]
    nibble = num & 0xf
    return num2bits[nibble] + count(num>>4)

def func(x,y):
    num = x ^ y
    return count(num)

print(func(3,2))
