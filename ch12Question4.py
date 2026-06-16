try:
    a = int(input("enter number one: "))
    b =  int(input("enter number two: "))
    print(a/b)
    
except ZeroDivisionError as e:
    print(e)