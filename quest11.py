def rec(nums,cpos,cres,res):
    if cpos==len(nums):
        res.append(cres[:])
        return
    rec(nums,cpos+1,cres,res)
    rec(nums,cpos+1,cres+[nums[cpos]],res)
    return

def func(nums):
    res=[]
    rec(nums,0,[],res)
    return res

nums = [1,2,3]
print(func(nums))
