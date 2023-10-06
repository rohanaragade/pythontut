class Add:
    def sum(self):
        print("addition is: ",self.a+self.b)
        print(f"addition is {self.a+self.b}")

num=Add()
ss=Add()
num.a=10
num.b=10
num.sum()
ss.a=23
ss.b=57
ss.sum()