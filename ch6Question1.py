first = int(input("Please enter number 1 : "))
second = int(input("Please enter number 2 : "))
third = int(input("Please enter number 3 : "))
fourth = int(input("Please enter number 4 : "))

if first > second and first > third and first > fourth :
    print(f"First number {first} is Greatest ")
elif second > first and second > third and second > fourth :
    print(f"Second number {second} is Greatest ")
elif third > first and third > second and third > fourth :
    print(f"Third number {third} is Greatest ")
elif fourth > first and fourth > third and fourth > second :
    print(f"Fourth number {fourth} is Greatest ")
    # not the best algo to solve this problem