tuple=(1,2,3,45,5)
for i in range(len(tuple)):
    print(tuple[i])

tuple=(1,2,3,45,5)
for i in tuple:
    print(i)

tuple1=(1,2,3,4,5) 
tuple2=(6,7,8)
tuple3=tuple1+tuple2
print(tuple3)

tuple1=(1,2,3)
tuple2=tuple1*3
print(tuple2)

t1=(1,3,6,7,8,9)
print(t1[2:5])

t1=(1,3,6,7,8,9)
print(t1[0:])
t1=(1,3,6,7,8,9)
print(t1[-1::-1])

t1=(1,3,6,7,8,9)
t2=t1[:]
print(t2)
