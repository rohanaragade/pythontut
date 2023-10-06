r=["ra","mk","mj","dn","an","mk","ra"]
v=input("enter the str you want to find the frequency:")
h=r.count(v)
print("frequency of world ",v,"is: ",h)

a=[]
for i in range(5):
    v=input("enter the string:")
    a.append(v)
print(a)

x=input("enter the str you want to find the count:")
c=a.count(x)
print("frequency of:",x,"is:",c)

a=[]
size=int(input("enetr the size of list: "))
for i in range(size):
    s=input("enter the no:")
    a.append(s)
print(a)
count=0
j=input("enter the value you have to  find frequency:")
for i in range(size):
    if(a[i]==j):
        count+=1
print(count)