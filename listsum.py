a=[]
size=int(input("enter the size of list you want:"))
for i in range(size):
    v=int(input("enter the list no:"))
    a.append(v)
print(a)
sum=0
for i in range(size):
    sum=sum+a[i]
print(sum)