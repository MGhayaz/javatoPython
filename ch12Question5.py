user = int(input("Number pls: "))
tables = [user*item for item in range(1,21)]
with open("ch12practicetable.txt","a") as w1:

    w1.write(str(tables) + "\n")

with open("ch12practicetable.txt","r") as r1:
    read = r1.read()
    print(read)