def func(digits):
    digits[-1] += 1
    i = len(digits)-1
    while i>=0 and digits[i]==10:
        digits[i] = 0
        if i==0:
            digits = [1]+digits
        else:
            digits[i-1] += 1
        i -= 1
    return digits

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int,input("\nEnter the digits: ").strip().split()))[:n]
print("Plus one:", func(arr))
    
