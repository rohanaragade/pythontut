class ty:
    clg="dyp"
    def __init__(self,name,roll,div):
        self.name = name
        self.rollno=roll
        self.division=div

    def printdetails(self):
        print(f"name of student is {self.name} his roll no is {self.rollno} having division {self.division} studing in {self.clg}")

a=ty('rohan',54,'A')
a.printdetails()