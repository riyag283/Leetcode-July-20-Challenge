def func(nums):
    result = [[]]
    for each in nums:
        result += [curr+[each] for curr in result]
    return result

# driver
nums = [1,2,3]
print(func(nums))
