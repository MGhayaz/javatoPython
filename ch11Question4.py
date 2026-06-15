class Complex:
    def __init__(self,rational, imaginery):
        self.rational = rational
        self.imaginary = imaginery
    def __add__(self,b):
        return Complex(self.rational + b.rational,self.imaginary + b.imaginary)    

    def __mul__(self,b):
        r = (self.rational*b.rational)-(self.imaginary*b.imaginary)
        i = (self.rational*b.imaginary)+(self.imaginary*b.rational)
        return Complex(r,i)
        # formula (ac−bd)+(ad+bc)i 

    def __str__(self):
        return f"{self.rational} + {self.imaginary}i"
a = Complex(1,2)
b = Complex(3,4)
print(a+b)
print(a*b)
        # ch11Question5,6,7 were skipped because their were not to relavant and different from above problem