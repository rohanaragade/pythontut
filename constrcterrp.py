class Calculator:
    def __init__(self,num):
        self.number=num
                    
    def squar(self):
        print(f"sqare of {self.number} is {self.number **2}")
    
    def squarroot(self):
        print(f"sqaroot of {self.number} is {self.number **0.5}")

    def cube(self):
        print(f"cube of {self.number} is {self.number **3}")

a=Calculator(4)
a.squar()
a.squarroot()
a.cube()