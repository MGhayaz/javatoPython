animals_fruits = ["donkey","lion","Apples"]
with open("ch9Question5text.txt", "r") as file:
    content = file.read()
    contentnew = content
for word in animals_fruits :
    contentnew = contentnew.replace(word, "****")

with open("ch9Question5text.txt", "w") as file:
    file.write(contentnew)