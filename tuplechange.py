a=("rohan",7,2002,3)
t=list(a)
t[1]="aragde"
a=tuple(t)
print(a)

a=("rohan",7,2002,"hii")
n=input("enter the str you want to check its exist or not:")
print(n in a)

a=("rohan",7,2002,"hii")
n=int(input("enter the str you want to check its exist or not:"))
if n in a:
    print("given string preset in tuple")
else:
    print("not present")

tuple1=("Fortuner","Endever","Gloster","x1")
print(tuple1)
del(tuple1)
print(tuple1)