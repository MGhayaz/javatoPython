class employees:
    company = "Microsoft"
    def __init__(self,name,salary,pin):
        self.name = name
        self.salary = salary
        self.pin = pin
p = employees("ghayaz","140000","500013")
print(p.name,p.salary,p.company,p.pin)           