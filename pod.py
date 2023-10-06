n=int(input("enter the no: "))
pro=1
while(n>0):
    pro=pro*(n%10)
    n=n//10
print("product of digits of no: ",pro)
