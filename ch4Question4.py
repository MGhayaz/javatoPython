numbers = []
i=0
while i < 5:
    runner = int(input("please enter (5) numbers to add : "))
    numbers.append(runner)
    i+=1
    
print(sum(numbers))