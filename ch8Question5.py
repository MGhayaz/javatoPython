def recursive(star):
    
    if star == 0 :
        print("")
        
    else :
        print("*"*star)
        recursive(star-1)
n = int(input("Number : "))
recursive(n)