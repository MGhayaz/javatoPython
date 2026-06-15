inpute =int(input("number de : "))
for i in range (2, inpute) : 
    if (inpute % i == 0) : 
        print("Not Prime")
        break
else : 
    print("Optimus is here")
    