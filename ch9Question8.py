with open("ch9Question8_Original.txt","r") as fileread : 
    content = fileread.read()
with open("ch9Question8_Copy.txt","w") as fileedit :
    for line in content:
        fileedit.write(line)
    print("New File made")    
