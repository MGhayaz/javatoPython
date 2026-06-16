from random import randint
class GuessNumber:
    def __init__(self):
        self.guess = randint(1,100)

    def play(self):
        self.greet()
        self.startGame()
        
    def greet(self):
        print("Welcome to guess the number challenge\nYou get Five(5) chances to guess right number")
    def takeInput(self):
        self.userinput = int(input("Please enter your guess: "))        

    def checkInput(self):
        if(self.userinput <= 0):
            print("invalid input entered")
            exit()
    def dif(self):
        difference = abs(self.userinput - self.guess)
        if difference <= 4 and self.userinput != self.guess:
            print("Too close bro")      
    def validateinput(self):
        if self.userinput == self.guess:
            print(f"Guessed Right! The number was {self.guess}")
            return True

        elif self.userinput < self.guess:
            print("Guess Higher")
        else:
            print("Guess Lower")

        return False         

    def startGame(self):
        for i in range(5):

            self.takeInput()
            self.checkInput()
            self.dif()

            if self.validateinput():
                return

        print(f"The number was: {self.guess}")
game = GuessNumber()
game.play()    

