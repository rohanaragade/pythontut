a=int(input("enter a:"))
b=int(input("enter b:"))
print("before swap value of a:",a)
print("before swap value of b:",b)
c=a
a=b
b=c
print("after swap value of a:",a)
print("after swap value of b:",b)

a=int(input('enter a:'))
b=int(input('enter b:'))
print('before a:',a)
print("before b:",b)
a=a+b
b=a-b
a=a-b

print('after a:',a)
print("after b:",b)