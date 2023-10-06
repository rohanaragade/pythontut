a=[]
for i in range(4):
    l=input("enter the string: ")
    a.append(l)
print(a)
index=int(input("enter the index where you want to insert the str: "))
value=input("enter the string: ")
a.insert(index,value)
print(a)

# x=["ro","rohn","ron",54,7]
# x.insert(2,"aragade")
# print(x)