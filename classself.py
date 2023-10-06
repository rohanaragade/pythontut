class ty:
    age=21
    def info(self):
        print("mysef",self.name,"styding in",self.clgname,'age is',self.age)
        print(f"myself {self.name} & I am styding in {self.clgname}",'age is',self.age)   

key=ty()
lock=ty()
key.name="ROHAN"
lock.name="RAHUL"
key.clgname="DYPCET"
lock.clgname="KIT"
key.info()
lock.info()
print(key.age)