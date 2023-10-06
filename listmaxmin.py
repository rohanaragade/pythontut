a=[]
size=int(input("enter the size: "))
for i in range(size):
    v=int(input("enter the nomburs:"))
    a.append(v)
print(a)
max=a[0]
min=a[0]
for i in range(size):
    if a[i]>max:
         max=a[i]
    if a[i]<min:
        min=a[i]
print(max)
# print(min)







 
    