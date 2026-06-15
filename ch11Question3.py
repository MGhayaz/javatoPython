class employee:
    salary = 500
    increment = 20
    @property
    def showcurrentsalary(self):
        return (self.salary + self.salary * (self.increment/100))
    @showcurrentsalary.setter
    def showcurrentsalary(self,salary):
        self.increment = ((salary/self.salary)-1)*100    

deepak = employee()
deepak.showcurrentsalary = 580
print(deepak.increment)


