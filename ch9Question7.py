with open("ch9Question6.txt","r") as file:
    lines =  file.readline()
    lineNumber = 1
    for line in lines:
        if("python","Python" in line ):
            print(f"python is present in line {lineNumber}") 
            break   
        lineNumber+=1
    else:
        print("Found Nothing")
