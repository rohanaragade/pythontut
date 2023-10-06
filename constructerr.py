class employee:
    def __init__(self,name):
        self.name=name

    def putdata(self,age):
        print("name of employee is: ",self.name,'& age is:',age)

rd=employee("Rohan")
rd.putdata(21)

