def func(nums,k):
    dict1 = {}
    for num in nums:
        dict1.setdefault(num,0)
        dict1[num] += 1
    list1 = list(zip(dict1.keys(),dict1.values()))
    list1.sort(key = lambda x:-x[1])
    return [x[0] for x in list1[:k]]    

print(func([1,1,1,2,2,3],2))
