n=int(input("enter the no you want:"))
reverse=0
temp=n
while(n>0):
    reverse=reverse*10+n%10
    n=n//10
if(temp==reverse):
    print("no is pallindrome")
else:
    print("not a palindromic number!")