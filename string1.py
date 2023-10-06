str = "rohan"
print(str)

str1 = input("enter your name:")
print(str1)


def string():
    str1 = input("enter your name:")
    print(str1)

string()

r = "ms dhoni"
for i in r:
    print(i,end="")   # end="" for in one line

r = "ms dhoni"
for i in range(len(r)):
    print(r[i],end="")

a = "rohan"+"aragde"
print(a)

b = 2*"rohan"
print(b)

c = "a"
d = "rohan"
print(c in d)

c = "a"
d = "rohan"
print(c not in d)

c = "a"
d = "rohan"
print(c != d)

l=10
m=10
print(l is m)