class A:
    def getdata(self):
        self.a=int(input("entert the value of a:"))
        self.b=int(input("entert the value of b:"))
    
class B(A):
    def add(self):
        
        print('addition is:',self.a+self.b)

# aa=A()
bb=B()
bb.getdata()
bb.add()