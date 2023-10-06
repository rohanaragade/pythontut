str=input("enter your name:")
for i in range(len(str)-1,-1,-1):
    print(str[i],end="")

str=input("\nenter your name:")
print(str[-1::-1])

print(str[len(str)-1::-1])

r='rohan'
for i in range(-1,-6,-1):
    print(r[i],end='')
