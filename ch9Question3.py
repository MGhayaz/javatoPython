print("Welcome to table maker : [2-20] ")

for j in range(2,21):
    filename = f"ch9Question3tables/table{j}.txt"
    try:    
        with open(filename,"x") as f:
            for i in range(1,21):
                f.write(f"{j} X {i} = {(j*i)}\n")
        print(f"printing table {j}")
    except FileExistsError:
        print(f"file for table {j} already Exists")    
