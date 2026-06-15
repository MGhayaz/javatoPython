import random

computer = random.choice([-1,0,1])
user = input("Welcome to Snake Water Gun Game\nChoose anyone [s/w/g]: ")
if(user == "s" or user == "w" or user == "g"):
    


    my_dict = {"s": -1, "w": 0, "g": 1}
    my_reversed_dict = {-1:"Snake",0: "Water",1: "Gun"}
    me = my_dict[user]
    print(f"You Choosed {my_reversed_dict[me]} And computer choosed {my_reversed_dict[computer]}")

    if(me == computer):
        print("draw")
    elif((me == -1 and computer == 0) or (me == 0 and computer == 1) or (me == 1 and computer == -1) ):
        print("you win")
    else : 
        print("You Lose")        
else: 
    print("Invalid Input entered")
    exit()        