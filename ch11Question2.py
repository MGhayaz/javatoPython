class animal:
    def __init__(self):
        pass
    def walk_live(self):
        print("Walking")
class pets(animal):
    def  love(self):
        print("I love my Master")
class dog(pets):
    def bark(self):
       print("Bow Bow")


germanSherpherd = dog()
germanSherpherd.bark()
germanSherpherd.love()
germanSherpherd.walk_live()        
        