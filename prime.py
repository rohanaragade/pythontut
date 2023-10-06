n=int(input("enter the no:"))
i=1
count=0
while(i<=n):
    if(n%i==0):
     count+=1
    i+=1
if(count==2):
    print("no is odd")
else:
    print("no is not odd")