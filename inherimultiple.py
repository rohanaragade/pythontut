class A:
    l=10
    def getdata(self):
        self.a=int(input("entert the value of a:"))
        self.b=int(input("entert the value of b:"))

class B():
    l=19
    def input(self):
        self.c=int(input("entert the value of c:"))

class D(A,B):
    def add(self):
        print('addition is:',self.a+self.b+self.c)


dd=D()
print(dd.l)
dd.getdata()
dd.input()
dd.add()
print(dd.l)
