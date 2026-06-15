from random import randint
class train:
    def __init__(self,trainno,fro,to):
        self.trainno = trainno
        self.fro = fro
        self.to = to
    def bookticket(self):
        return f"{self.trainno} train ticket booked from {self.fro},to {self.to}"
    def status(self):
        return f"{self.trainno} train from {self.fro},to {self.to} is running late by 1hr"
    @staticmethod
    def getfare():
        return f"Fare : {randint(125,8788)}"
    
o = train("12332","hawdah","nasik")
print(f"{o.getfare()}, {o.status()}, {o.bookticket()}")