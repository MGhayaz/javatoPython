class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"i =  {self.i}, j = {self.j}")

class ThreeDvector(twoDvector):
    def __init__(self, i, j,k):
        super().__init__(i, j) # two d vector ke constructor ke through uske operations idar chalaye as well as apne threedvector ke bi chalaye
        self.k = k 
    def show(self):
        print(f"i = {self.i}, j = {self.j}, k = {self.k}")  

a = twoDvector(1,1)
b = ThreeDvector(5,5,5)
a.show()
b.show()                    