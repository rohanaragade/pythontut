n=int(input("enter the no:"))
i=1
sum=0
while(i<=n):
    sum+=i
    i+=1
print(sum)

j=int(input("enter the no upto you want find sum :"))
i=1
sum=0
while(i<=j):
    sum+=(i*i)
    i+=1
print(sum)

n=int(input("enter the no:"))
i=1
sum=0
while(i<=n):
    if(i%2==0):
      sum+=i
    i+=1
print(sum)
