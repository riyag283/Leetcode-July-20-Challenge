def func(nums):
    k = 0
    for i in nums:
        k^=i
    k = k&~(k-1)
    a,b = 0,0
    for i in nums:
        if(i&k):
            a^=i
        else:
            b^=i
    return [a,b]

nums = [1,2,1,3,2,5]
print(func(nums))
