with open("ch9Question6.txt","r") as stringline:
    fullstringline = stringline.read()
    if("python" in (fullstringline.lower()) ):
        count = fullstringline.lower().count("python")
        print(f"python word exists {count} times")
    else:
        print("does not exist")    