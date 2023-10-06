# NANR
def add():
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a+b
    print("sum of two no is: ",c)
add()

# WANR
def add(x,y):
    c=x+y
    print("sum of two no is: ",c)
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
add(a,b)

# NAWR
def add():
    a=int(input("enter the value of a:"))
    b=int(input("enter the value of b:"))
    c=a+b
    return c
x=add()
print("sum of two no is: ",x)

# WAWR
def add(x,y):
    c=x+y
    return c
a=int(input("enter the value of a:"))
b=int(input("enter the value of b:"))
add(a,b)
print("sum of two no is: ",add(a,b))
