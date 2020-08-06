def func(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high-low)//2
        if nums[mid]==nums[high]:
            high -= 1
        elif nums[mid]>nums[high]:
            low = mid+1
        else:
            high = mid
    return nums[high]

nums = [2,2,2,0,1]
print(func(nums))
