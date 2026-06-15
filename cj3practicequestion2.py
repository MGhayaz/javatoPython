from datetime import date

name = input("please enter your name : ")
Today = str(date.today())
letter = '''Greetings <|name|>,
            you are selected as SDE 2 at Amazon
            <|Date|>
'''
print(letter.replace("<|name|>", name).replace("<|Date|>",Today))