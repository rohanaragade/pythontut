a=[]
for i in range(4):
    l=input("enter the string: ")
    a.append(l)
print(a)
value=input("enter the value you want to remove: ")
a.remove(value)
print(a)