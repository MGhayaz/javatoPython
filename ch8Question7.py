# not very important question, it was just use of method with list
def rem(l,word):
    for item in l:
        l.remove(word)
        return l

l = ["harry", "rohan","ghayaz","an"]
inpute = input("name to remove : ")
print(rem(l,inpute))