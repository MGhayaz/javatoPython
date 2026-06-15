def greatmethod(a,b,c,d):
    if a > b and a > c and a > d :
        print(f"First number {a} is Greatest ")
    elif b > a and b > c and b > d :
        print(f"Second number {b} is Greatest ")
    elif c > a and c > b and c > d :
        print(f"Third number {c} is Greatest ")
    elif d > a and d > c and d > b :
        print(f"Fourth number {d} is Greatest ")
    # not the best algo to solve this problem

a = int(input("Number : "))
b = int(input("Number : "))
c = int(input("Number : "))
d = int(input("Number : "))

greatmethod(a,b,c,d)