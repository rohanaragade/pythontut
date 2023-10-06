def add(a):
    return a+a
print(add(5))

x=lambda l:l+l
print(x(5))

c= lambda x,y : x*y
print(c(5,4))  

z= lambda a,b,c : (a+b)/c
print(z(5,7,6))

def sexi(n):
    return lambda a: a*n

mydoubler=sexi(2)
print(mydoubler(11))

def sexi(n):
    return lambda a: a*n

mytripler=sexi(3)
print(mytripler(11))

def sexi(n):
    return lambda a: a*n

r=sexi(3)
print(r(11))