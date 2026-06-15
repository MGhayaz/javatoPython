def lengthConverter(inches):
    cm = (2.54*inches) 
    return cm
inch = int(input("inches pls: "))
print(f"cms are {lengthConverter(inch)}")