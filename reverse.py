n=int(input("enter the no: "))
sum=0
while(n>0):
    sum=sum*10+(n%10)
    n=n//10
print("reverse of no is: ",sum)