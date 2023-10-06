class A:
   
    def put(self):
        self.a=10
class B(A):
    
    def putd(self):
        self.b=45

class C(B):
    def add(self):
        print("addition is: ",self.a+self.b)


cc=C()
cc.put()
cc.putd()
cc.add()


