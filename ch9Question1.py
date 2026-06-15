with open("poem_for_ch9.txt","r") as poem:
    fullpoem = poem.read()
    if("twinkle" in (fullpoem.lower()) ):
        count = fullpoem.lower().count("twinkle")
        print(f"Twinkle word exists {count} times")
    else:
        print("does not exist")    