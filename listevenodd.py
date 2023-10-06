a=[]
size=int(input("enter the size: "))
for i in range(size):
    v=int(input("enter the nomburs:"))
    a.append(v)
print(a)
even=0
odd=0
for i in range(size):
    if(a[i]%2==0):
        even+=1
    else:
        odd+=1
print("even no are: ",even)
print("odd no are: ",odd)