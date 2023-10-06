n=int(input("enter the no: "))
sum=0
temp=n
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10
if(temp==sum):
    print("no is armstrong")
else:
    print("no is not armstrong")