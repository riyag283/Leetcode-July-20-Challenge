def func(digits):
    digits[-1] += 1
    for i in range(len(digits)-2,-1,-1):
        if digits[i+1] > 9:
            digits[i] += 1
            digits[i+1] -= 10
        else:
            break
        print(digits)
    if digits[0] > 9:
        digits[0] = 0
        digits = [1] + digits
    return digits

# Driver code
n = int(input("Enter number of elements: "))
arr = list(map(int,input("\nEnter the digits: ").strip().split()))[:n]
print("Plus one:", func(arr))
    
