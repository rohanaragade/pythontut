class person:
    country='india'
    def breadth(self):
        print("breathing...")

class emp(person):
    com='honda'
    
    def salary(self):
        print(f"salary is {self.salary}")

    def breadth(self):
        print("breathing in emp...")

class programmer(emp):
    com='cognizent'

    def printde(self):
        print("i am in programmer class")

pp=programmer()
ee=emp()
pp.breadth()
pp.printde()
# ee.salary()
ee.breadth()
print(pp.country)