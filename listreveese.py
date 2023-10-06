a=[]
for i in range(5):
    x=int(input("enter the noubers: "))
    a.append(x)
print(a)
a.reverse()
print("revese of list is: ",a)

a=[]
size=int(input("enter the size:"))
for i in range(size):
    c=input("enter the no:")
    a.append(c)
print(a)
i=0
j=size-1
while(i<j):
    temp=a[i]
    a[i]=a[j]
    a[j]=temp
    i+=1
    j-=1
print("reverse list is: ",a)