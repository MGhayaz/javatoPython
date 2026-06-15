with open("ch9Question4DonkeyFile.txt","r") as poem:
    fullpoem = poem.read()
    if("donkey" in (fullpoem.lower()) ):
        count = fullpoem.lower().count("donkey")
        fullpoem = fullpoem.replace("donkey", "###")
        with open("ch9Question4DonkeyFile.txt","w") as swap:
            swap.write(fullpoem)
        print(f"donkey word replaced with ### {count} times")
    else:
        print("donkey word does not exist")   