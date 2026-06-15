class Calculator : 
    number = 0
    def __init__(self, number):
        self.number = int(number)
    def square(self):
        return (self.number * self.number)  
    def cube(self):
        return (self.number * self.number * self.number)
    def squareroot(self):
        return (self.number ** 0.5)
    @staticmethod # fourth Question
    def greet():
        return("Greetings Commander")

num = Calculator(input("enter number to find square, cube, square root : "))
print(f"{num.greet()}\nSquare: {num.square()} , Cube : {num.cube()}, SquareRoot : {num.squareroot()}")       