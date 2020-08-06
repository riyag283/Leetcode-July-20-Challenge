def func(n):
    ugly = [0]*n
    ugly[0] = 1

    i2, i3, i5 = 0, 0, 0
    mul2, mul3, mul5 = 2, 3, 5

    for i in range(1,n):
        minm = min(mul2,mul3,mul5)
        ugly[i] = minm
        if minm == mul2:
            i2 += 1
            mul2 = ugly[i2]*2
        elif minm == mul3:
            i3 += 1
            mul3 = ugly[i3]*3
        else:
            i5 += 1
            mul5 = ugly[i5]*5
        print(i)
        print(i2,i3,i5)
        print(mul2,mul3,mul5)
    print(ugly)
    return ugly[-1]

# Driver
print("Nth ugly",func(10))
