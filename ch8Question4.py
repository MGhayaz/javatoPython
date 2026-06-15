def recursive(n):
    
    if n == 0 or n ==1:
        return 1
    else :
        sum = n + (recursive(n-1))
    return sum
n = int(input("Number : "))
print(recursive(n))